import os

PRODUCER_CONFIG = {
    "bootstrap.servers": os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS",
        "localhost:9092"
    ),
    "client.id": "instacart-producer",

    "acks": "all",

    "enable.idempotence": True,

    "compression.type": "snappy",

    "linger.ms": 20,

    "batch.num.messages": 10000,

    "queue.buffering.max.messages": 200000
}