import logging
import pytest

from retaillake.logging.logger_factory import LoggerFactory


def test_logger_factory_returns_logger():
    logger = LoggerFactory.get_logger("unit-test")

    assert isinstance(logger, logging.Logger)


def test_logger_name():
    logger = LoggerFactory.get_logger("runtime")

    assert logger.name == "runtime"


def test_logger_is_singleton():
    logger1 = LoggerFactory.get_logger("runtime")
    logger2 = LoggerFactory.get_logger("runtime")

    assert logger1 is logger2


def test_logger_has_handlers():
    logger = LoggerFactory.get_logger("runtime")

    assert len(logger.handlers) > 0


def test_logger_level():
    logger = LoggerFactory.get_logger("runtime")

    assert logger.level in (
        logging.INFO,
        logging.DEBUG,
        logging.WARNING,
    )


def test_multiple_loggers_are_distinct():
    logger1 = LoggerFactory.get_logger("runtime")
    logger2 = LoggerFactory.get_logger("spark")

    assert logger1.name != logger2.name


def test_logger_propagation_disabled():
    logger = LoggerFactory.get_logger("runtime")

    assert logger.propagate is False



def test_get_logger_returns_same_instance():
    logger1 = LoggerFactory.get_logger("retaillake")
    logger2 = LoggerFactory.get_logger("retaillake")

    assert logger1 is logger2


def test_logger_level_is_valid():
    logger = LoggerFactory.get_logger("retaillake")

    assert logger.level in (
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    )