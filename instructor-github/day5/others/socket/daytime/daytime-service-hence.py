""" a quick demo of daytime service """
import socket
import commands
HOST = socket.gethostname()                 # Symbolic name meaning the local host
PORT = 32132


while 1:
#creating the socket object 
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    """Running an example several times with too small delay between executions, 
	could lead to this error:

    	socket.error: [Errno 98] Address already in use
    This is because the previous execution has left the socket in a TIME_WAIT state, and can’t be immediately reused."""

    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to address - the socket becomes access able  
    s.bind((HOST, PORT))
    s.listen(5)   

    # Listen for connections made to the socket, 
    # Its argumnets specifies the maximum number of queued connections (0, 5)


    # Accept a connection   
    conn, addr = s.accept()
    print 'Connected by', addr 
    conn.send(commands.getoutput('date'))
    conn.close()
  except Exception ,e :
    #conn.close()
    print e

