from datetime import datetime

from retaillake.logging.logger_factory import LoggerFactory


logger = LoggerFactory.get_logger(__name__)


class PlatformObservability:

    @staticmethod
    def startup(name):

        logger.info("=" * 60)

        logger.info(
            f"Pipeline Started : {name}"
        )

        logger.info(
            f"Timestamp : {datetime.now()}"
        )

        logger.info("=" * 60)

    @staticmethod
    def shutdown(name):

        logger.info("=" * 60)

        logger.info(
            f"Pipeline Finished : {name}"
        )

        logger.info(
            f"Timestamp : {datetime.now()}"
        )

        logger.info("=" * 60)

    @staticmethod
    def log_metrics(metrics):

        logger.info(

            f"Pipeline Metrics : {metrics.summary()}"

        )

    @staticmethod
    def log_health(result):

        logger.info(

            f"Health : {result}"

        )