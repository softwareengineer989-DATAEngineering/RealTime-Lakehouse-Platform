from retaillake.validation.validators import (
    BronzeValidator,
    SilverValidator,
    GoldValidator,
)


def main():

    validators = [

        BronzeValidator(),

        SilverValidator(),

        GoldValidator(),

    ]

    for validator in validators:

        result = validator.validate()

        print("=" * 60)

        print(result.component)

        print(result.passed)

        print(result.message)

        print(result.metrics)


if __name__ == "__main__":

    main()