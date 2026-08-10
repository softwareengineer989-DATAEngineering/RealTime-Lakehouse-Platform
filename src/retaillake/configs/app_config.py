from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATASETS = PROJECT_ROOT / "datasets"
LOGS = PROJECT_ROOT / "logs"
DOCS = PROJECT_ROOT / "docs"
SCRIPTS = PROJECT_ROOT / "scripts"

APP_NAME = "RealTime Lakehouse Platform"

PRODUCER_NAME = "instacart-producer"
CONSUMER_NAME = "instacart-consumer"

PRODUCER_LOGGER = "KafkaProducer"
CONSUMER_LOGGER = "KafkaConsumer"
PROCESSOR_LOGGER = "OrderProcessor"


CHECKPOINTS = PROJECT_ROOT / "checkpoints"

BRONZE = DATASETS.parent / "data" / "bronze"

STREAM_BATCH_SIZE = 500

STREAM_DELAY = 0.01

METRICS_INTERVAL = 10000

HEARTBEAT_INTERVAL = 30

DEV_MODE = True

