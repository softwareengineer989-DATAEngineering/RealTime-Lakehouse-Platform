"""
Central logging constants.

Every logging module imports values from here instead of
hardcoding strings.
"""

DEFAULT_LOG_LEVEL = "INFO"

DEFAULT_LOG_DIRECTORY = "logs"

DEFAULT_LOG_FILE = "retaillake.log"

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

CONSOLE_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

FILE_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

MAX_LOG_FILE_SIZE = 10 * 1024 * 1024

BACKUP_COUNT = 5