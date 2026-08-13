"""
Enterprise Kafka Exception Hierarchy

Sprint 11
"""

class KafkaPlatformError(Exception):
    """
    Base exception for all Kafka platform errors.
    """

    pass


class KafkaConfigurationError(KafkaPlatformError):
    """
    Raised when Kafka configuration is invalid.
    """

    pass


class KafkaProducerError(KafkaPlatformError):
    """
    Raised for producer failures.
    """

    pass


class KafkaConsumerError(KafkaPlatformError):
    """
    Raised for consumer failures.
    """

    pass


class KafkaSerializationError(KafkaPlatformError):
    """
    Raised when serialization fails.
    """

    pass


class KafkaTopicError(KafkaPlatformError):
    """
    Raised for topic management failures.
    """

    pass