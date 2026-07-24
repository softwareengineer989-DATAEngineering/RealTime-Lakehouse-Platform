import signal
import time

from confluent_kafka import Consumer

from retaillake.kafka.consumer.config import CONSUMER_CONFIG
from retaillake.kafka.consumer.deserializer import deserialize
from retaillake.kafka.consumer.process_orders import process

from retaillake.configs.kafka_config import TOPICS
from retaillake.utils.logger import get_logger
from retaillake.utils.constants import (
    POLL_INTERVAL,
    LOG_INTERVAL,
    TEST_RECORD_LIMIT
)
from retaillake.configs.app_config import CONSUMER_LOGGER
from retaillake.configs.app_config import DEV_MODE
from retaillake.kafka.metrics.consumer_metrics import ConsumerMetrics

from retaillake.kafka.consumer.retry_processor import process_with_retry

logger = get_logger(CONSUMER_LOGGER)

running = True

def shutdown(sig, frame):
    global running
    running = False


signal.signal(signal.SIGINT, shutdown)

consumer = Consumer(CONSUMER_CONFIG)

consumer.subscribe([
    TOPICS["orders_raw"]
])


def main():

    global running

    metrics = ConsumerMetrics()

    processed = 0

    start = time.time()

    try:

        while running:

            msg = consumer.poll(POLL_INTERVAL)

            if msg is None:
                continue

            if msg.error():
                logger.error(msg.error())
                continue

            record = deserialize(msg.value())

            process_with_retry(record)

            metrics.increment()

            consumer.commit(msg)

            processed += 1

            if processed % LOG_INTERVAL == 0:

                logger.info(
                    f"Consumed {processed:,} records"
                )

            if DEV_MODE and processed >= TEST_RECORD_LIMIT:
                logger.info(
                    f"DEV MODE: stopping after {processed:,} records."
                )

                break

    finally:

        consumer.close()

    elapsed = time.time() - start

    logger.info("=" * 60)

    logger.info("Consumer Finished")

    logger.info(f"Records : {processed:,}")

    logger.info(f"Time : {elapsed:.2f}")

    logger.info(
        f"Rate : {processed/elapsed:.2f} msg/sec"
    )

    metrics.report()

    logger.info("=" * 60)


if __name__ == "__main__":

    main()