from retaillake.spark.gold.gold_stream import read_silver_stream
from retaillake.spark.gold.transformations import transform
from retaillake.spark.gold.gold_writer import write_gold


def run():

    silver_df = read_silver_stream()

    gold_df = transform(silver_df)

    query = write_gold(gold_df)

    query.awaitTermination()

if __name__ == "__main__":
    run()