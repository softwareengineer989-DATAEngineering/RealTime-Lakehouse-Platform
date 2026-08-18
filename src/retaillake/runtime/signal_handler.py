import signal

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class SignalHandler:

    def __init__(self):
        self.shutdown_requested = False

    def _handle_signal(self, signum, frame):
        logger.warning("=" * 80)
        logger.warning(f"Received signal {signum}. Shutdown requested.")
        logger.warning("=" * 80)

        self.shutdown_requested = True

    def register(self):

        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

        logger.info("Signal handlers registered.")