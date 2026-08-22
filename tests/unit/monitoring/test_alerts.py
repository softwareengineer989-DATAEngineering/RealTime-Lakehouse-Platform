from retaillake.monitoring.alert_manager import AlertManager


def main():

    alerts = AlertManager()

    alerts.info(
        "Recovery",
        "Recovery initialized."
    )

    alerts.warning(
        "Kafka",
        "Consumer lag increasing."
    )

    alerts.error(
        "Checkpoint",
        "Checkpoint write failed."
    )

    alerts.critical(
        "Streaming",
        "Streaming query terminated."
    )

    print("Alert Test Passed")


if __name__ == "__main__":
    main()