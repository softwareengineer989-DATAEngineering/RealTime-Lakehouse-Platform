import os
from retaillake.spark.session.spark_session import get_spark

def read_kafka_stream(topic=None):

    spark = get_spark()

    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:29092")

    topic = topic or os.getenv("KAFKA_TOPIC_ORDERS", "orders.raw")


    return (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", bootstrap_servers)
        .option("subscribe", topic)
        .option("startingOffsets", "earliest")
        .load()
    )