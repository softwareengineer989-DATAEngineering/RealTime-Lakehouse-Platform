from retaillake.configs.app_config import CONSUMER_NAME
from retaillake.configs.kafka_defaults import (
    BOOTSTRAP_SERVERS,
    TOPICS
)

CONSUMER_CONFIG = {

    "bootstrap.servers": BOOTSTRAP_SERVERS,

    "group.id": CONSUMER_NAME,

    "auto.offset.reset": "earliest",

    "enable.auto.commit": False,

    "session.timeout.ms": 45000,

    "max.poll.interval.ms": 300000

}

TOPIC = TOPICS["orders_raw"]

