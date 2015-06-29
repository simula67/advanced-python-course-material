#!/bin/bash

#Simplified Wrapper and Interface Generator

swig -python example.i

gcc -c -fpic example.c example_wrap.c  -I/usr/include/python2.7/

ld -shared example.o example_wrap.o -o _example.so

