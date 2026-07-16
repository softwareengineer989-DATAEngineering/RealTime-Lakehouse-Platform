from confluent_kafka.admin import AdminClient

admin = AdminClient(
    {
        "bootstrap.servers": "localhost:9092"
    }
)

metadata = admin.list_topics(timeout=10)

for topic in metadata.topics.values():

    print("=" * 50)

    print(topic.topic)

    print(f"Partitions : {len(topic.partitions)}")