import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request[0].rstrip()
        client_sock = self.request[1]
        print self.data
        client_sock.sendto(self.data.upper(), self.client_address )

if __name__ == "__main__":
    HOST, PORT = "localhost", 9001

    server = SocketServer.UDPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
