from retaillake.configs.app_config import DATASETS

USE_SAMPLE_DATA = True

SAMPLE_ORDERS = DATASETS / "sample" / "orders_100k.csv"

FULL_ORDERS = DATASETS / "raw" / "instacart" / "orders.csv"


def get_orders_dataset():

    if USE_SAMPLE_DATA:
        return SAMPLE_ORDERS

    return FULL_ORDERS