from socket import *
from config import *
from pickle import *
import sys

# Receiving Server Address from commandline
def serverAddr():
    if len(sys.argv) < 2:
        DEST = "127.0.0.1"
    else:
        DEST = sys.argv[1]
        #checking if input address is correct
        while True:
            try:
                gethostbyaddr(DEST)
                break
            except:
                print "Enter Correct Server Address: ",
                DEST = raw_input()
                if DEST == "":
                    DEST = "127.0.0.1"
                    break
    return DEST

# Client Communication with server                
def clientComm(DEST):
    # Socket for receiving arbitrary input
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    host = (DEST, SERVER_PORT)
    sock.connect(host)

    # Taking Arbitrary Data and Converting into String to
    # be sent over Socket using Pickle dumps
    ARBDATA = dumps(raw_input("Enter Arbitrary Data to Send to Server: \n"))

    # Receiving arbitrary data from Server
    data = sock.sendall(ARBDATA)
    
    sock.close()

if __name__ == '__main__':
    DEST = serverAddr()
    clientComm(DEST)
