from retaillake.configs.app_config import PROCESSOR_LOGGER
from retaillake.utils.logger import get_logger
# import random
logger = get_logger(PROCESSOR_LOGGER)


def process(record):


    logger.info(

        f"Order={record['order_id']} "

        f"User={record['user_id']}"

    )