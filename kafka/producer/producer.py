from confluent_kafka import Producer

from kafka.producer.config import PRODUCER_CONFIG

producer = Producer(PRODUCER_CONFIG)