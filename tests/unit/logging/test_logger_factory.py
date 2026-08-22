# from retaillake.logging.logger_factory import LoggerFactory
#
#
# logger = LoggerFactory.get_logger(__name__)
#
# logger.debug("Debug message")
#
# logger.info("Information message")
#
# logger.warning("Warning message")
#
# logger.error("Error message")
#
# logger.critical("Critical message")



from retaillake.logging.logger_factory import LoggerFactory


def test_logger_factory_returns_logger():

    logger = LoggerFactory.get_logger(__name__)

    assert logger is not None


def test_logger_name():

    logger = LoggerFactory.get_logger("RetailLake")

    assert logger.name == "RetailLake"


def test_logger_has_info():

    logger = LoggerFactory.get_logger(__name__)

    assert hasattr(logger, "info")


def test_logger_has_warning():

    logger = LoggerFactory.get_logger(__name__)

    assert hasattr(logger, "warning")


def test_logger_has_error():

    logger = LoggerFactory.get_logger(__name__)

    assert hasattr(logger, "error")