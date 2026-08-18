from retaillake.runtime.shutdown import GracefulShutdown


def test_shutdown_creation():

    manager = GracefulShutdown()

    assert manager.timeout == 30