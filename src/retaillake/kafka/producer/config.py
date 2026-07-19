from retaillake.configs.kafka_config import BOOTSTRAP_SERVERS
from retaillake.configs.app_config import PRODUCER_NAME

PRODUCER_CONFIG = {

    "bootstrap.servers": BOOTSTRAP_SERVERS,

    "client.id": PRODUCER_NAME,

    "acks": "all",

    "enable.idempotence": True,

    "compression.type": "snappy",

    "linger.ms": 20,

    "batch.num.messages": 10000,

    "queue.buffering.max.messages": 200000

}