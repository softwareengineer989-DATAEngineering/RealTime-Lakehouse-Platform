import time

from pyspark.sql.streaming import StreamingQuery
from retaillake.monitoring.alert_manager import AlertManager
from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)

alerts = AlertManager()
class GracefulShutdown:

    def __init__(self, timeout=30):
        self.timeout = timeout

    def stop_query(self, query: StreamingQuery):

        if query is None:
            return

        logger.info("=" * 80)
        logger.info("Stopping Streaming Query...")
        logger.info("=" * 80)

        start = time.time()

        query.stop()

        while query.isActive:

            if time.time() - start > self.timeout:

                logger.warning(
                    "Shutdown timeout exceeded."
                )

                break

            time.sleep(1)

        logger.info("Streaming Query stopped.")

        alerts.warning(
            "Shutdown",
            "Streaming query stopped gracefully."
        )