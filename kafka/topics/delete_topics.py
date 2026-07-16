from confluent_kafka.admin import AdminClient

from topic_config import TOPICS

admin = AdminClient(
    {
        "bootstrap.servers": "localhost:9092"
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