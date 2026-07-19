from confluent_kafka.admin import AdminClient

from retaillake.kafka.topics.topic_config import TOPICS
from retaillake.configs.kafka_config import BOOTSTRAP_SERVERS

admin = AdminClient(
    {
        "bootstrap.servers": BOOTSTRAP_SERVERS
    }
)

result = admin.delete_topics(
    [t["name"] for t in TOPICS]
)

for topic, future in result.items():

    try:

        future.result()

        print(f"Deleted {topic}")

    except Exception as e:

        print(e)