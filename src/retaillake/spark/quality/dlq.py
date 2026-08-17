from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def split_valid_invalid(
    dataframe: DataFrame,
):
    """
    Split stream into

    valid

    invalid

    records.
    """

    valid_dataframe = dataframe.filter(
        col("is_valid")
    )

    invalid_dataframe = dataframe.filter(
        ~col("is_valid")
    )

    return (

        valid_dataframe,

        invalid_dataframe,

    )

