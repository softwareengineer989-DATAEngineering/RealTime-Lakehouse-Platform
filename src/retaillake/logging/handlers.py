"""
Logging handler builders.
"""

import logging

from logging.handlers import RotatingFileHandler

from pathlib import Path

from retaillake.logging.constants import (
    DEFAULT_LOG_DIRECTORY,
    DEFAULT_LOG_FILE,
    MAX_LOG_FILE_SIZE,
    BACKUP_COUNT,
)

from retaillake.logging.formatter import (
    build_console_formatter,
    build_file_formatter,
)


def build_console_handler() -> logging.StreamHandler:
    """
    Console handler.
    """

    handler = logging.StreamHandler()

    handler.setFormatter(
        build_console_formatter()
    )

    return handler


def build_rotating_file_handler() -> RotatingFileHandler:
    """
    Rotating application log.
    """

    log_directory = Path(DEFAULT_LOG_DIRECTORY)

    log_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    logfile = log_directory / DEFAULT_LOG_FILE

    handler = RotatingFileHandler(
        logfile,
        maxBytes=MAX_LOG_FILE_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )

    handler.setFormatter(
        build_file_formatter()
    )

    return handler