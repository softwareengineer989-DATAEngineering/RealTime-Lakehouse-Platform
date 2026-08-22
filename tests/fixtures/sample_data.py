"""
Reusable sample datasets.
"""

import pytest


@pytest.fixture
def sample_orders():

    return [

        {

            "order_id": 1,

            "customer_id": 101,

            "amount": 250.0

        },

        {

            "order_id": 2,

            "customer_id": 102,

            "amount": 500.0

        },

        {

            "order_id": 3,

            "customer_id": 103,

            "amount": 125.0

        }

    ]