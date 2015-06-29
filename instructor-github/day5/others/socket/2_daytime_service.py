#/bin/env python 

""" client application for daytime services """

import socket


#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#now connect to the web server on port 80
# - the normal http port
s.connect(('localhost', 13))
#its creates a port in the client and connects to remote port mentioned in the connect function. 


#retriving the data from server
data = ""
while 1:
    t = s.recv(25)
    if not t:
        break
    data += t

print data.rstrip()  # striping new line char. 

