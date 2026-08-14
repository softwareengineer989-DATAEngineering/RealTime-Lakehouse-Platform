from retaillake.kafka.producer.delivery_report import delivery_report
from retaillake.kafka.producer.partitioner import get_message_key
from retaillake.kafka.producer.producer_factory import ProducerFactory
from retaillake.kafka.producer.serializer import serialize

from retaillake.logging.logger_factory import LoggerFactory


class ProducerService:

    def __init__(self):

        self.logger = LoggerFactory.get_logger(__name__)

        self.producer = ProducerFactory.create()

    def publish(self, topic: str, record: dict):

        self.producer.produce(
            topic=topic,
            key=get_message_key(record),
            value=serialize(record),
            callback=delivery_report
        )

    def poll(self):

        self.producer.poll(0)

    def flush(self):

        self.logger.info(
            "Flushing producer."
        )

        self.producer.flush()