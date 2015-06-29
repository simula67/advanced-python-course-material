__author__ = 'ravi'
import logging

log1 = logging.getLogger('Logger-1')
log1.setLevel(logging.DEBUG)

log_format= "%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(message)s"
log_fmt = logging.Formatter(fmt=log_format)

sh = logging.StreamHandler()
sh.setFormatter(log_fmt)

fh = logging.FileHandler('/tmp/hp.log')
fh.setFormatter(log_fmt)

log1.addHandler(sh)
log1.addHandler(fh)

log1.debug('a sample debug message')
log1.error('a sample error message')
#log1.debug('a sample debug message')
#log1.debug('a sample debug message')

