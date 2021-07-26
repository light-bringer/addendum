import logging
from logging.handlers import RotatingFileHandler


def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=200000, backupCount=5)
    logging.basicConfig(handlers=[handler], format='[%(asctime)s]: %(name)s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s')
    log = logger
    return log


Log = create_rotating_log('logs/app.log')
