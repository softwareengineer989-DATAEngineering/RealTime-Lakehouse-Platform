"""
Formatter builders.

Responsible only for constructing log formatters.
"""

import logging

from retaillake.logging.constants import (
    CONSOLE_FORMAT,
    FILE_FORMAT,
    DATE_FORMAT,
)


def build_console_formatter() -> logging.Formatter:
    """
    Formatter used for console output.
    """

    return logging.Formatter(
        fmt=CONSOLE_FORMAT,
        datefmt=DATE_FORMAT,
    )


def build_file_formatter() -> logging.Formatter:
    """
    Formatter used for log files.
    """

    return logging.Formatter(
        fmt=FILE_FORMAT,
        datefmt=DATE_FORMAT,
    )