#!/usr/bin/env python
import telnetlib

hostname = 'localhost'
port = 9013

t = telnetlib.Telnet(hostname, port)
t.write('\n')
t.write('read \n')
print t.read_all()

