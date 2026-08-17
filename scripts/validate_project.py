from pathlib import Path
import traceback

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)

logger.info(
    "RetailLake validation started."
)

def check(name, func):
    logger.info(f"Running validation: {name}")

    print(f"[CHECK] {name}")

    try:
        func()

        logger.info(f"{name} validation passed")

        print(f"[PASS] {name}\n")

    except Exception:

        logger.exception(f"{name} validation failed")

        print(f"[FAIL] {name}")

        traceback.print_exc()

        print()


def validate_configs():
    from retaillake.configs.app_config import PROJECT_ROOT
    from retaillake.configs.kafka_defaults import TOPICS
    from retaillake.configs.datasets import get_orders_dataset

    print(PROJECT_ROOT)
    print(TOPICS)
    print(get_orders_dataset())


def validate_logger():
    from retaillake.utils.logger import get_logger

    logger = get_logger("Validation")
    logger.info("Logger OK")


def validate_producer():
    from retaillake.kafka.producer.producer import producer

    print(type(producer))


def validate_consumer():
    from retaillake.kafka.consumer.consumer import consumer

    print(type(consumer))


def validate_topics():
    from retaillake.kafka.topics.topic_config import TOPICS

    print(TOPICS)


def validate_dataset():
    from retaillake.configs.datasets import get_orders_dataset

    path = Path(get_orders_dataset())

    print(path)

    assert path.exists()



def validate_streaming():
    from retaillake.kafka.streaming.stream_engine import is_running

    print(is_running())





def validate_shutdown():
    from retaillake.kafka.streaming.shutdown import register_shutdown

    print(register_shutdown)


def validate_heartbeat():
    from retaillake.kafka.monitoring.heartbeat import start

    print(start)

def validate_consumer_metrics():

    from retaillake.kafka.metrics.consumer_metrics import ConsumerMetrics

    print(ConsumerMetrics)


if __name__ == "__main__":

    print("=" * 70)
    print("RetailLake Validation")
    print("=" * 70)

    check("Configs", validate_configs)
    check("Logger", validate_logger)
    check("Producer", validate_producer)
    check("Consumer", validate_consumer)
    check("Consumer Metrics", validate_consumer_metrics)
    check("Topics", validate_topics)
    check("Dataset", validate_dataset)

    check("Streaming Engine", validate_streaming)

    check("Shutdown", validate_shutdown)

    check("Heartbeat", validate_heartbeat)

    print("=" * 70)
    print("Validation Complete")
    print("=" * 70)

