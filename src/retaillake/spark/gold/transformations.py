from retaillake.spark.gold.aggregations import build_customer_metrics
from retaillake.spark.gold.metrics import calculate_metrics


def transform(df):
    """
    Execute Gold transformations.
    """

    df = build_customer_metrics(df)

    df = calculate_metrics(df)

    # Temporary Console debugging.
    print(df.columns)

    return df