__author__ = 'antonjoj'
import logging

logger = logging.getLogger("Logger-1")
logger.setLevel(logging.DEBUG)

log_format = "%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(message)s"
log_fmt = logging.Formatter(fmt=log_format)

sh = logging.StreamHandler()
sh.setFormatter(log_fmt)

fh = logging.FileHandler('hp.log')
fh.setFormatter(log_fmt)

logger.addHandler(sh)
logger.addHandler(fh)

logger.debug('a sample debug message')
logger.debug('a sample debug message')
logger.debug('a sample debug message')
