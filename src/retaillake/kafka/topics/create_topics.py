from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import NewTopic

from retaillake.kafka.topics.topic_config import TOPICS
from retaillake.configs.kafka_defaults import BOOTSTRAP_SERVERS


admin = AdminClient(
    {
        "bootstrap.servers": BOOTSTRAP_SERVER
    }
)

topics = []

for topic in TOPICS:

    topics.append(

        NewTopic(

            topic=topic["name"],

            num_partitions=topic["partitions"],

            replication_factor=topic["replication_factor"]

        )

    )

fs = admin.create_topics(topics)

for topic, future in fs.items():

    try:

        future.result()

        print(f"Created {topic}")

    except Exception as e:

        print(f"{topic}: {e}")