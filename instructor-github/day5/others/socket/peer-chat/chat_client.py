# Echo client program

import socket

HOST = 'fosslab.linuxpert.in'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    s.send(raw_input("Mesg: "))
    data = s.recv(1024)
    print "Mesg:" , data


s.close()
