#!/bin/env python 

import logging


#logging.basicConfig(level= logging.DEBUG)

log1 = logging.getLogger('test_log')
log1.setLevel(logging.WARNING)


#handler 
sh = logging.StreamHandler()
fmt_obj = logging.Formatter("%(name)s %(levelname)s %(filename)s  %(process)d %(message)s")
sh.setFormatter(fmt_obj)
log1.addHandler(sh)


log2 = logging.getLogger('test_warn')
log2.setLevel(logging.WARNING)
fh = logging.FileHandler(__file__+'log')
fh.setFormatter(fmt_obj)
log2.addHandler(fh)



log1.debug('a note of log')
log1.warning('a note of log')
log2.debug('a note of log')
log2.warning('a note of log')






