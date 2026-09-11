"""Logging utilities for ABAP AI Code Generator"""

import logging
import sys
from typing import Optional


class Logger:
    """Centralized logging configuration."""

    _loggers = {}

    @staticmethod
    def get_logger(name: str, level: str = "INFO") -> logging.Logger:
        """Get or create a logger with the specified name and level."""
        if name in Logger._loggers:
            return Logger._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level))

        # Console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(getattr(logging, level))

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        Logger._loggers[name] = logger

        return logger
