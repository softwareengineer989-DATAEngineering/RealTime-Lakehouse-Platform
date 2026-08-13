from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)

logger.debug("Debug message")

logger.info("Information message")

logger.warning("Warning message")

logger.error("Error message")

logger.critical("Critical message")