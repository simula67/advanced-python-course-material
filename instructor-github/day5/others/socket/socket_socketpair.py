#!/usr/bin/env python

"""Parent/child communication through a socket pair.
"""
#end_pymotw_header

import socket
import os
import time
parent, child = socket.socketpair()

pid = os.fork()

if pid:
    time.sleep(8)
    print 'Print\nin parent, sending message'
    child.close()
    parent.sendall('ping')
    response = parent.recv(1024)
    print 'P:response from child:', response
    parent.close()
    

else:
    print 'Child\nin child, waiting for message'
    parent.close()
    message = child.recv(1024)
    print 'message from parent:', message
    child.sendall('pong')
    child.close()
