from retaillake.monitoring.alert_manager import AlertManager


def test_alert_manager_creation():
    manager = AlertManager()

    assert manager is not None