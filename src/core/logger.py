import logging
import logging.handlers
import queue
import sys
from collections.abc import MutableMapping
from typing import Any, cast

import structlog
from structlog.typing import Processor

# A global queue for non-blocking logging
log_queue: queue.Queue[Any] = queue.Queue(-1)


def redact_sensitive_data(
    _: object, __: str, event_dict: MutableMapping[str, Any]
) -> MutableMapping[str, Any]:
    """Simple processor to redact sensitive fields."""
    sensitive_fields = {"password", "token", "secret", "authorization"}
    for field in sensitive_fields:
        if field in event_dict:
            event_dict[field] = "***"
    return event_dict


def setup_logging(debug: bool = False, log_level: str = "INFO") -> None:
    """
    Configures structlog to be non-blocking using a QueueHandler.

    - dev: Pretty console logs (Rich)
    - prod: JSON logs
    """

    processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
        redact_sensitive_data,
        structlog.processors.StackInfoRenderer(),
    ]

    if debug:
        renderer = structlog.dev.ConsoleRenderer(colors=True)
        processors.append(renderer)
    else:
        processors.append(structlog.processors.JSONRenderer())

    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    handler = logging.StreamHandler(sys.stdout)

    queue_handler = logging.handlers.QueueHandler(log_queue)

    root_logger = logging.getLogger()
    root_logger.addHandler(queue_handler)
    root_logger.setLevel(log_level.upper())

    listener = logging.handlers.QueueListener(log_queue, handler)
    listener.start()

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    return cast(structlog.stdlib.BoundLogger, structlog.get_logger(name))
