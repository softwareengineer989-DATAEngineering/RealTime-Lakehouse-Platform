from retaillake.configuration.config_loader import load_configuration
from retaillake.configuration.validator import validate_configuration
from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def main():

    try:
        config = load_configuration()

        logger.info(
            "Configuration loaded."
        )

        validate_configuration(config)

        logger.info(
            "Configuration validation succeeded."
        )

        print()

        print("=" * 70)
        print("CONFIGURATION VALIDATION SUCCESS")
        print("=" * 70)

        print(f"Application : {config['application']['name']}")
        print(f"Version     : {config['application']['version']}")
        print(f"Environment : {config['environment']['name']}")
        print(f"Spark App   : {config['spark']['app_name']}")
        print(f"Kafka Topic : {config['kafka']['topic']}")

        print("=" * 70)
        print("Configuration successfully validated.")
        print("=" * 70)

    except Exception as e:

        logger.exception(
            "Configuration validation failed."
        )

        print()
        print("=" * 60)
        print("CONFIGURATION VALIDATION FAILED")
        print("=" * 60)

        print(f"{type(e).__name__}: {e}")

        raise SystemExit(1)

if __name__ == "__main__":
    main()