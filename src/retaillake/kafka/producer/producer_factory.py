from confluent_kafka import Producer

from retaillake.kafka.config.kafka_config import KafkaConfig
from retaillake.logging.logger_factory import LoggerFactory


class ProducerFactory:
    """
    Enterprise Producer Factory.

    Responsible for constructing Kafka producers
    from validated platform configuration.
    """

    _logger = LoggerFactory.get_logger(__name__)

    @classmethod
    def create(cls) -> Producer:

        config = KafkaConfig()

        producer = Producer(
            config.producer_settings()
        )

        cls._logger.info(
            "Kafka Producer successfully created."
        )

        return producer