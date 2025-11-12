import logging
import logging.config
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

import helper
""""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')"""

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e,exc_info=True)