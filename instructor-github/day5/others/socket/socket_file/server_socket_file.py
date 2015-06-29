import socket
import os
import sys

s  = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
t_file = 'sock_file'


s.bind(t_file)
s.listen(1)

#print '/proc/'+str(os.getpid())+'/fd/'
#os.system('ls -l /proc/'+str(os.getpid())+'/fd/')

conn, addr = s.accept()
conn.send(raw_input('Enter the data:'))

os.unlink(t_file)
s.close()

