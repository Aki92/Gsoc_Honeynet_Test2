from socket import *
from config import *
from pickle import *
from thread import *

""" Server Class Handling both Clients by receiving data
    from Client 1 and then sending data to Client 2.

    Have functionality of Threading for Client 2 so that
    it can connect anytime with server
"""
class Server(object):
    def __init__(self):
        self.DATA = ""
        self.send_connection = None

    # Handling Client1 Connection and receiving data
    def recvClient(self):
        # Socket for reading arbitrary data from client 1
        self.recv_socket = socket(AF_INET, SOCK_STREAM)
        self.recv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        host = (SERVER_HOST, SERVER_PORT)
        self.recv_socket.bind(host)
        self.recv_socket.listen(1)

        # Accepting connection from Client 1
        self.recv_connection, self.recvclient_address = self.recv_socket.accept()

        temp = ""
        # Receiving DATA from client1
        while True:
            data = self.recv_connection.recv(BUFSIZE)
            if not data:
                break
            temp += data

        self.DATA = temp
        print 'Data Received from Client1 and Forwarded to Client2: \n' + \
        str(loads(self.DATA))

        # Closing the socket
        self.recv_socket.close()

    # Handling Client2 Connection and sending data
    def sendClient(self):
        # Socket for reading arbitrary data from client 1
        self.send_socket = socket(AF_INET, SOCK_STREAM)
        self.send_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        host = (SERVER_HOST, SERVER_PORT + 50)
        self.send_socket.bind(host)
        self.send_socket.listen(1)

        # Accepting connection from Client 1
        self.send_connection, self.sendclient_address = self.send_socket.accept()

        # Closing the socket
        self.send_socket.close()

    # Waiting for Client1 to send data and Client2 to connect
    def wait(self):
        while self.DATA == "" or self.send_connection == None:
            continue

        # Sending data to Client2
        self.send_connection.send(self.DATA)

        # Closing both sockets
        self.recv_socket.close()
        self.send_socket.close()
    
if __name__ == '__main__':
    # Making Server Class Object
    server = Server()
    
    # Starting thread for Handling Client1
    start_new_thread(server.sendClient,())

    # Handling Client1
    server.recvClient()
    
    # Waiting for Client1 to send data
    server.wait()
