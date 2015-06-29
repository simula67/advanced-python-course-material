#!/bin/env python 
# myapp.py

import logging



def config():
     logging.basicConfig(filename='myapp.log', level=logging.INFO)

if __name__ == '__main__':
    config()
