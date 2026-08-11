from retaillake.spark.silver.silver_stream import read_bronze_stream
from retaillake.spark.quality.validation import validate
from retaillake.spark.quality.dlq import split_valid_invalid
from retaillake.spark.silver.transformations import transform
from retaillake.spark.silver.silver_writer import write_silver

def run():

    bronze_df = read_bronze_stream()

    # Validate incoming records
    validated = validate(bronze_df)

    # Split into valid / invalid
    valid_df, invalid_df = split_valid_invalid(validated)

    # Transform only valid records
    transformed = transform(valid_df)

    query = write_silver(transformed)

    query.awaitTermination()


if __name__ == "__main__":
    run()