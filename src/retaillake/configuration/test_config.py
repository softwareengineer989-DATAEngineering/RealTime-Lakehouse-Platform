from retaillake.configuration.config_loader import load_configuration
from retaillake.configuration.validator import validate_configuration


def main():

    try:

        config = load_configuration()

        validate_configuration(config)

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

        print()
        print("=" * 60)
        print("CONFIGURATION VALIDATION FAILED")
        print("=" * 60)

        print(f"{type(e).__name__}: {e}")

        raise SystemExit(1)


if __name__ == "__main__":
    main()