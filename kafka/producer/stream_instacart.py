import os
import time

import pandas as pd
from confluent_kafka import Producer

from kafka.producer.config import PRODUCER_CONFIG
from kafka.producer.delivery_report import delivery_report
from kafka.producer.partitioner import get_message_key
from kafka.producer.serializer import serialize

TOPIC = os.getenv("KAFKA_TOPIC_ORDERS", "orders.raw")

DATASET = os.getenv(
    "DATASET_PATH",
    "datasets/sample/orders_100k.csv"
)

CHUNK_SIZE = 10000

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

        if processed % 1000 == 0:
            producer.poll(0)

        if processed % 10000 == 0:
            print(f"Processed {processed:,} records")

producer.flush()

elapsed = time.time() - start

print("=" * 60)
print("Producer Finished")
print(f"Records : {processed:,}")
print(f"Time    : {elapsed:.2f} sec")
print(f"Rate    : {processed / elapsed:.2f} msg/sec")
print("=" * 60)