from socket import *
from config import *
from pickle import *


if __name__ == '__main__':
    # Socket for reading arbitrary data from client 1
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    host = (SERVER_HOST, SERVER_PORT)
    sock.bind(host)
    sock.listen(1)
    
    # Accepting connection from Client 1
    rec_conn, addr = sock.accept()
    ARBDATA = rec_conn.recv(BUFSIZE)
    print 'Data Received from Client1 and Forwarded to Client2: \n' + str(loads(ARBDATA))
    
    # Socket for writing(forwarding) arbitrary data to client 2
    sendsock = socket(AF_INET, SOCK_STREAM)
    sendsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    host = (SERVER_HOST, SERVER_PORT + 50)
    sendsock.bind(host)
    sendsock.listen(1)

    send_conn, addr = sendsock.accept() 
    send_conn.send(ARBDATA)
    
    sock.close()
    sendsock.close()
