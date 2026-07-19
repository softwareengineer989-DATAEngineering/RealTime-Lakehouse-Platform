import os

BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

TOPICS = {

    "orders_raw": "orders.raw",

    "orders_validated": "orders.validated",

    "orders_deadletter": "orders.deadletter",

    "customers_raw": "customers.raw",

    "inventory_events": "inventory.events",

    "platform_audit": "platform.audit"

}