from retaillake.configuration.config_loader import load_configuration

from retaillake.kafka.exceptions import KafkaConfigurationError


class KafkaConfig:

    def __init__(self):

        config = load_configuration()

        self.bootstrap_servers = config["kafka"].get("bootstrap_servers")
        self.topic = config["kafka"].get("topic")

        if not self.bootstrap_servers:
            raise KafkaConfigurationError(
                "Kafka bootstrap_servers is empty."
            )

        if not self.topic:
            raise KafkaConfigurationError(
                "Kafka topic is empty."
            )

    def producer_settings(self):

        return {
            "bootstrap.servers": self.bootstrap_servers,
            "enable.idempotence": True,
            "acks": "all",
            "compression.type": "snappy",
            "linger.ms": 20,
        }