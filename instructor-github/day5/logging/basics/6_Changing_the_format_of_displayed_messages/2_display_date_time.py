#!/bin/env python 

import logging
#logging.basicConfig(format='%(asctime)s %(message)s')
#logging.warning('is when this event was logged.')

#logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d-%m-%Y')
logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(process)s] %(message)s')
logging.warning('is when this event.')
