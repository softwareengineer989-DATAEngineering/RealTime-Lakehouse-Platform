from retaillake.configuration.environment import get_environment
from retaillake.spark.session.spark_session import SparkSessionFactory


def test_spark_session_uses_environment():
    env = get_environment()

    spark = SparkSessionFactory()

    assert env is not None
    assert spark is not None