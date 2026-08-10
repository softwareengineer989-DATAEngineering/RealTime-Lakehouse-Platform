from pyspark.sql.functions import col, from_json

from retaillake.spark.streaming.kafka_source import read_kafka_stream
from retaillake.spark.schemas.order_schemas import ORDER_SCHEMA
from retaillake.spark.bronze.bronze_writer import write_bronze


def run():

    kafka_df = read_kafka_stream()

#Original Version
    parsed = (
        kafka_df
        .selectExpr("CAST(value AS STRING)")
        .select(
            from_json(
                col("value"),
                ORDER_SCHEMA
            ).alias("data")
        )
        .select("data.*")
    )

    query = write_bronze(parsed)

#Debugging version below -
    # parsed = (
    #     kafka_df
    #     .selectExpr(
    #         "CAST(key AS STRING) AS key",
    #         "CAST(value AS STRING) AS value"
    #     )
    # )
    #
    # query = (
    #     parsed.writeStream
    #     .format("console")
    #     .outputMode("append")
    #     .option("truncate", "false")
    #     .start()
    # )

    query.awaitTermination()


if __name__ == "__main__":
    run()
