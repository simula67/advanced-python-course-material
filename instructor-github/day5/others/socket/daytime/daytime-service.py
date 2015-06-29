""" a quick demo of daytime service """
import socket
import commands
HOST = socket.gethostname()  # Symbolic name meaning the local host
PORT = 32132

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)   
while 1:
#creating the socket object 
  try:
    conn, addr = s.accept()
    # here 
    #	conn - client socket object 
    #   addr - (ip-addr, port of the client socket) 
    print 'Connected by', addr, ":", conn 
    conn.send(commands.getoutput('date'))
    conn.close()
  except Exception ,e :
    #conn.close()
    print e

