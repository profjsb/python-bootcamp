import logging
LOG_FILENAME = 'loggin1.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.WARNING)

def make_logs():
    logging.debug('This is a debug message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
