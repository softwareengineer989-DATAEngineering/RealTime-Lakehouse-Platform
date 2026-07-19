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


logger = get_logger("Producer")

TOPIC = TOPICS["orders_raw"]

DATASET = get_orders_dataset()



producer = Producer(PRODUCER_CONFIG)

processed = 0

start = time.time()


for chunk in pd.read_csv(DATASET, chunksize=CHUNK_SIZE):

    for _, row in chunk.iterrows():

        record = row.to_dict()

        producer.produce(

            topic=TOPIC,

            key=get_message_key(record),

            value=serialize(record),

            callback=delivery_report

        )

        processed += 1

        if processed % PRODUCER_POLL_INTERVAL == 0:
            producer.poll(0)

        if processed % LOG_INTERVAL == 0:
            logger.info(
                f"Processed {processed:,} records"
            )


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