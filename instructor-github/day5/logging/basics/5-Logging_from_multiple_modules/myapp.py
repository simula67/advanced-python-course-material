#!/bin/env python 
# myapp.py
import logging
import log_config
import mylib

def demo(): 
   logging.info('Started')
   mylib.do_something()
   logging.info('Finished')

if __name__ == '__main__':
    log_config.config()
    demo();
