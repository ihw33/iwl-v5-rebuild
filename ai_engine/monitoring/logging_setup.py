from __future__ import annotations

import logging
from typing import Any


def get_logger(name: str = "ai_engine", level: str = "INFO") -> Any:
    try:
        import structlog
        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer("message"),
                structlog.processors.JSONRenderer(),
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )
        logger = structlog.get_logger(name)
        logging.getLogger().setLevel(getattr(logging, level.upper(), logging.INFO))
        return logger
    except Exception:
        logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO), format="%(asctime)s %(levelname)s %(name)s %(message)s")
        return logging.getLogger(name)

