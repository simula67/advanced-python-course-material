__author__ = 'antonjoj'

import logging
import logging.handlers
LOG_FILE = "logging.log"

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)


handler = logging.handlers.RotatingFileHandler( LOG_FILE, maxBytes=20, backupCount=5)

my_logger.addHandler(handler)


for i in range(20):
    my_logger.debug("i = {}".format(i))
