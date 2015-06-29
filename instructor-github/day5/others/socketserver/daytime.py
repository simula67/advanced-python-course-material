import SocketServer
import time

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.request.sendall(time.strftime("%d-%m-%Y %H:%M:%S"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9013

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
