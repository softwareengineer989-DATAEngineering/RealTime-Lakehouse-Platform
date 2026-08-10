APP_NAME = "RealTime-Lakehouse-Platform"

# Dataset locations
SAMPLE_DATASET = "datasets/sample/orders_100k.csv"
FULL_DATASET = "datasets/raw/instacart/orders.csv"

# Streaming configuration
CHUNK_SIZE = 10000
POLL_INTERVAL = 1.0

# Logging
LOG_INTERVAL = 10000

# Kafka Producer
PRODUCER_POLL_INTERVAL = 1000

# Local development safety limit
TEST_RECORD_LIMIT = 20

DEFAULT_ENCODING = "utf-8"

SHUTDOWN_TIMEOUT = 5

SPARK_APP_NAME = "RealTime-Lakehouse-Platform"

CHECKPOINT_LOCATION = "/app/checkpoints/bronze"

BRONZE_PATH = "/app/data/bronze"