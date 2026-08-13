"""
Enterprise Logger Factory.

Responsible for creating and caching logger instances.
"""

from __future__ import annotations

import logging

from retaillake.logging.constants import DEFAULT_LOG_LEVEL

from retaillake.logging.handlers import (
    build_console_handler,
    build_rotating_file_handler,
)


class LoggerFactory:
    """
    Creates singleton logger instances.

    Prevents duplicate handlers and ensures consistent
    logging configuration across the platform.
    """

    _loggers: dict[str, logging.Logger] = {}

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:

        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)

        logger.setLevel(DEFAULT_LOG_LEVEL)

        logger.propagate = False

        if not logger.handlers:

            logger.addHandler(
                build_console_handler()
            )

            logger.addHandler(
                build_rotating_file_handler()
            )

        cls._loggers[name] = logger

        return logger