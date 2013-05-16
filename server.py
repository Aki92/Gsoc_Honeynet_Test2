from socket import *
from config import *
from pickle import *
from thread import *

# Variable for checking if Client2 has connected 
send_conn = None

# Handling Client2 Connection and sending data
def handleClient():
    global send_conn
    send_conn, addr = sendsock.accept()
            
if __name__ == '__main__':
    # Socket for reading arbitrary data from client 1
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    host = (SERVER_HOST, SERVER_PORT)
    sock.bind(host)
    sock.listen(1)
    
    # Socket for reading arbitrary data from client 1
    sendsock = socket(AF_INET, SOCK_STREAM)
    sendsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    host = (SERVER_HOST, SERVER_PORT + 50)
    sendsock.bind(host)
    sendsock.listen(1)
    
    # Starting thread for Client2 to Connect at anytime
    start_new_thread(handleClient,())
    
    # Accepting connection from Client 1
    rec_conn, addr = sock.accept()
    ARBDATA = rec_conn.recv(BUFSIZE)
    print 'Data Received from Client1 and Forwarded to Client2: \n' + \
           str(loads(ARBDATA))

    # Waiting for Client2 to Connect with Server
    while send_conn == None: 
        continue
    
    # Sending data to Client2
    send_conn.send(ARBDATA)
    
    # Closing the socket
    sock.close()
