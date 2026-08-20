from datetime import datetime

from retaillake.logging.logger_factory import LoggerFactory

from .alert_levels import AlertLevel


logger = LoggerFactory.get_logger(__name__)


class AlertManager:

    def __init__(self):
        pass

    def send(
        self,
        level: AlertLevel,
        component: str,
        message: str,
    ):

        banner = "=" * 80

        logger.warning(banner)
        logger.warning(f"ALERT LEVEL : {level.value}")
        logger.warning(f"TIME        : {datetime.utcnow()}")
        logger.warning(f"COMPONENT   : {component}")
        logger.warning(f"MESSAGE     : {message}")
        logger.warning(banner)

    def info(self, component, message):
        self.send(AlertLevel.INFO, component, message)

    def warning(self, component, message):
        self.send(AlertLevel.WARNING, component, message)

    def error(self, component, message):
        self.send(AlertLevel.ERROR, component, message)

    def critical(self, component, message):
        self.send(AlertLevel.CRITICAL, component, message)