from confluent_kafka.admin import AdminClient
from retaillake.kafka.topics.topic_config import TOPICS

from retaillake.configs.kafka_defaults import BOOTSTRAP_SERVERS
admin = AdminClient(
    {
        "bootstrap.servers": BOOTSTRAP_SERVERS
    }
)

metadata = admin.list_topics(timeout=10)

for topic in metadata.topics.values():

    print("=" * 50)

    print(topic.topic)

    print(f"Partitions : {len(topic.partitions)}")