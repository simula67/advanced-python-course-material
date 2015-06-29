# Echo client program
import time
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
bsend = time.time()
s.send('Hello, world')
data = s.recv(1024)
arecv = time.time()
s.close()
print 'Received', repr(data)
print "Time taken : ", (arecv-bsend) 
