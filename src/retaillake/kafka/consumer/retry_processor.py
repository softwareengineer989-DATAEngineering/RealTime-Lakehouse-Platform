from retaillake.kafka.consumer.retry_policy import retry

from retaillake.kafka.consumer.process_orders import process


def process_with_retry(record):

    retry(

        process,

        record

    )