from retaillake.configs.kafka_config import BOOTSTRAP_SERVERS
from retaillake.configs.app_config import CONSUMER_NAME

CONSUMER_CONFIG = {

    "bootstrap.servers": BOOTSTRAP_SERVERS,

    "group.id": CONSUMER_NAME,

    "auto.offset.reset": "earliest",

    "enable.auto.commit": False

}