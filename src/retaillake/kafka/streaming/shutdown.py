import signal

from retaillake.kafka.streaming.stream_engine import stop
from retaillake.utils.logger import get_logger

logger = get_logger("Shutdown")


def shutdown_handler(signum, frame):
    logger.info("Shutdown signal received.")
    stop()


def register_shutdown():
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)