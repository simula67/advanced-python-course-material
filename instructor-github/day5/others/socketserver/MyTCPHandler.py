import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = ''

        for temp in self.request.recv(1024):
            data += temp

        print "{} wrote: {}".format(self.client_address[0], data)
        self.request.sendall(data.upper())


def main():
    HOST, PORT = "localhost", 9912
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()