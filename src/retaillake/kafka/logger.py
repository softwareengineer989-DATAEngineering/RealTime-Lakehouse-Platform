from retaillake.logging.logger_factory import LoggerFactory


def get_kafka_logger(name):

    return LoggerFactory.get_logger(name)