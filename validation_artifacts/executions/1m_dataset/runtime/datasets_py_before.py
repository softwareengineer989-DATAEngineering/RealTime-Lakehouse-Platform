"""
Enterprise Dataset Configuration

Sprint 16

Provides centralized dataset profile management for all
validation stages.

Supported Profiles

100K
500K
1M
FULL
"""

import os

from retaillake.configs.app_config import DATASETS

DATASET_PROFILES = {
    "100K": DATASETS / "sample" / "orders_100k.csv",
    "500K": DATASETS / "sample" / "orders_500k.csv",
    "1M": DATASETS / "sample" / "orders_1m.csv",
    "FULL": DATASETS / "raw" / "instacart" / "orders.csv",
}

DEFAULT_PROFILE = os.getenv(
    "DATASET_PROFILE",
    "500K",
).upper()


def get_dataset_profile() -> str:
    """
    Return active dataset profile.
    """

    if DEFAULT_PROFILE not in DATASET_PROFILES:
        raise ValueError(
            f"Unknown DATASET_PROFILE: {DEFAULT_PROFILE}"
        )

    return DEFAULT_PROFILE


def get_orders_dataset():
    """
    Return dataset path.
    """

    profile = get_dataset_profile()

    return DATASET_PROFILES[profile]