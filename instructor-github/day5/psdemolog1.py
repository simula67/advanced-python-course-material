__author__ = 'ravi'

import logging
fmt= "%(asctime)s:%(levelname)s:%(process)s:%(message)s"

logging.basicConfig(level=logging.DEBUG, format=fmt,
                    filename="testit.log")

logging.debug('debug message')
logging.info('a note on information')
logging.warn('warning note')
logging.error('error message')
logging.critical('critical error')

