import time

import pandas as pd
from confluent_kafka import Producer

from retaillake.configs.datasets import get_orders_dataset
from retaillake.configs.kafka_config import TOPICS

from retaillake.kafka.producer.config import PRODUCER_CONFIG
from retaillake.kafka.producer.delivery_report import delivery_report
from retaillake.kafka.producer.partitioner import get_message_key
from retaillake.kafka.producer.serializer import serialize

from retaillake.utils.logger import get_logger
from retaillake.utils.constants import (
    CHUNK_SIZE,
    LOG_INTERVAL,
    PRODUCER_POLL_INTERVAL
)

from retaillake.kafka.metrics.producer_metrics import ProducerMetrics
# from retaillake.kafka.streaming.stream_engine import is_running

from retaillake.kafka.streaming.stream_engine import is_running
from retaillake.kafka.streaming.shutdown import register_shutdown
from retaillake.kafka.monitoring.heartbeat import start

from retaillake.configs.app_config import PRODUCER_LOGGER

logger = get_logger(PRODUCER_LOGGER)


TOPIC = TOPICS["orders_raw"]

DATASET = get_orders_dataset()

register_shutdown()

start()

producer = Producer(PRODUCER_CONFIG)
metrics = ProducerMetrics()

processed = 0

start = time.time()


for chunk in pd.read_csv(
        DATASET,
        chunksize=CHUNK_SIZE
):

    if not is_running():
        break

    for _, row in chunk.iterrows():

        if not is_running():
            break

        record = row.to_dict()

        producer.produce(

            topic=TOPIC,

            key=get_message_key(record),

            value=serialize(record),

            callback=delivery_report

        )

        metrics.increment()

        processed += 1

        if processed % PRODUCER_POLL_INTERVAL == 0:
            producer.poll(0)

        if processed % LOG_INTERVAL == 0:
            logger.info(
                f"Processed {processed:,} records"
            )

metrics.report()

logger.info("Waiting for Producer Flush...")

producer.flush()

elapsed = time.time() - start


logger.info("=" * 60)

logger.info("Producer Finished")

logger.info(f"Records : {processed:,}")

logger.info(f"Time : {elapsed:.2f} sec")

logger.info(
    f"Rate : {processed/elapsed:.2f} msg/sec"
)

logger.info("=" * 60)