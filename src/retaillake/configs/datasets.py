import os

from retaillake.configs.app_config import DATASETS

SAMPLE_DATASETS = {
    "100K": DATASETS / "sample" / "orders_100k.csv",
    "500K": DATASETS / "sample" / "orders_500k.csv",
    "1M": DATASETS / "sample" / "orders_1m.csv",
    "FULL": DATASETS / "raw" / "instacart" / "orders.csv",
}


def get_dataset_profile() -> str:
    """
    Active dataset profile.

    Environment variable:

        DATASET_PROFILE

    Allowed:

        100K
        500K
        1M
        FULL

    Default

        100K
    """

    return os.getenv("DATASET_PROFILE", "100K").upper()


def get_orders_dataset():

    profile = get_dataset_profile()

    if profile not in SAMPLE_DATASETS:
        raise ValueError(
            f"Unsupported DATASET_PROFILE '{profile}'. "
            f"Allowed: {list(SAMPLE_DATASETS.keys())}"
        )

    return SAMPLE_DATASETS[profile]