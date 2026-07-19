from confluent_kafka import Producer

from retaillake.kafka.producer.config import PRODUCER_CONFIG

from retaillake.configs.app_config import PRODUCER_LOGGER

from retaillake.utils.logger import get_logger

logger = get_logger(PRODUCER_LOGGER)

producer = Producer(PRODUCER_CONFIG)