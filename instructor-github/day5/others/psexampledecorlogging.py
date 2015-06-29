__author__ = 'ravi'
import logging
logging.basicConfig(level=logging.DEBUG, )

def logger(message=''):
    def log_action(f):
        def call_function(*args, **kwargs):
            logging.debug('[{}]: {}: {}'.format(message, f.__name__, args))

            return f(args[0], args[1])
        return call_function
    return log_action

@logger()
def sum(a, b):
    return a + b

print sum(10, 11)
