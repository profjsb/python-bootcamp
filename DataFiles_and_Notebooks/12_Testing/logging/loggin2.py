import logging
logger = logging.getLogger("some_identifier")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.stream = open("loggin2.log", 'w')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

def make_logs():
    logger.info("This is an info message")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
