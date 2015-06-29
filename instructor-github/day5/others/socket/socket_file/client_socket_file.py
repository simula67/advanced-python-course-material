import socket

s  = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
t_file = 'sock_file'

s.connect(t_file)

data = ''

while 1:
   data = s.recv(10)
   if not data: break
   print data
   data = None

s.close()

