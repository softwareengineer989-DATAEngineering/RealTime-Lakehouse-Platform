def delivery_report(err, msg):

    if err:

        print(f"Delivery failed: {err}")

    else:

        print(
            f"Delivered "
            f"{msg.topic()} "
            f"Partition={msg.partition()} "
            f"Offset={msg.offset()}"
        )