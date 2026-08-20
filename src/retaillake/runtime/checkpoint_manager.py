from pathlib import Path

from retaillake.configs.app_config import CHECKPOINTS

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class CheckpointManager:
    """
    Enterprise Checkpoint Manager.

    Responsibilities

    • Create checkpoint directory
    • Validate checkpoint
    • Report health
    """

    def __init__(self, checkpoint_path: Path = CHECKPOINTS):
        self.checkpoint_path = Path(checkpoint_path)

    def ensure_exists(self) -> None:

        if not self.checkpoint_path.exists():

            logger.warning("=" * 80)
            logger.warning("Checkpoint directory not found.")
            logger.warning("Creating checkpoint directory...")
            logger.warning("=" * 80)

            self.checkpoint_path.mkdir(
                parents=True,
                exist_ok=True
            )

        logger.info(
            f"Checkpoint Location : {self.checkpoint_path}"
        )

    def validate(self) -> bool:

        if not self.checkpoint_path.exists():

            logger.error(
                "Checkpoint directory missing."
            )

            return False

        logger.info(
            "Checkpoint validation successful."
        )

        return True

    def health(self) -> dict:

        return {
            "path": str(self.checkpoint_path),
            "exists": self.checkpoint_path.exists()
        }