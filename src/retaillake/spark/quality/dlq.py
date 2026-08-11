from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def split_valid_invalid(df: DataFrame):
    """
    Split validated stream into
    valid and invalid records.
    """

    valid = df.filter(col("is_valid"))

    invalid = df.filter(~col("is_valid"))

    return valid, invalid