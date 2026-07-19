TOPICS = [

    {
        "name": "orders.raw",
        "partitions": 6,
        "replication_factor": 1
    },

    {
        "name": "orders.validated",
        "partitions": 6,
        "replication_factor": 1
    },

    {
        "name": "orders.deadletter",
        "partitions": 3,
        "replication_factor": 1
    },

    {
        "name": "customers.raw",
        "partitions": 3,
        "replication_factor": 1
    },

    {
        "name": "inventory.events",
        "partitions": 3,
        "replication_factor": 1
    },

    {
        "name": "platform.audit",
        "partitions": 1,
        "replication_factor": 1
    }

]