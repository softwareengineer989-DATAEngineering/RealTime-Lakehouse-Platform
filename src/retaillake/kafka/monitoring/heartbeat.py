import threading
import time

from retaillake.kafka.streaming.stream_engine import is_running
from retaillake.utils.logger import get_logger

logger = get_logger("Heartbeat")


def heartbeat(interval=30):

    while is_running():

        logger.info("Producer heartbeat OK")

        time.sleep(interval)


def start():

    thread = threading.Thread(
        target=heartbeat,
        daemon=True
    )

    thread.start()