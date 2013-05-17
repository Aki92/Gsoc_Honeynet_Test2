from socket import *
from config import *
from pickle import *
import argparse
import os

""" Parsing the Command Line Arguments by using ArgParse Module"""

# Checking if host entered exists or not
class check_host(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            gethostbyaddr(values)
            setattr(namespace, self.dest, values)
        except:
            pass
        
# Checking if file entered exists or not
class check_file(argparse.Action):
    def __call__(self, parser,namespace, values, option_string=None):
        if os.path.exists(values):
            setattr(namespace, self.dest, values)
        else:
            parser.error('Please enter Correct File Name')

# Description of Command Line arguments
parser = argparse.ArgumentParser(description='Takes Server Address and Client Type.')

# Optional Argument for Server Address
parser.add_argument('--host',default='127.0.0.1', type=str, action=check_host,
                   help='Server Address to Connect with (default value : 127.0.0.1)')

# Mutually Exclusive Group for Client Type with Send & Recv options
client_type = parser.add_mutually_exclusive_group(required=True)
client_type.add_argument('--send', type=str, action=check_file,
                        help='Client Send File to Server')
client_type.add_argument('--recv', action='store_true',
                        help='Client Receive File from Server')

""" Main Client Code """
class Client(object):
    """ Initializing variables"""
    def __init__(self, host, opt, filename=""):
        self.host = host
        # Setting Server Port acco. to Client Type
        if opt == 'send':
            self.port = SERVER_PORT
            self.filename = filename
        elif opt == 'recv':
            self.port = SERVER_PORT+50
        self.connectServer()

    """ Connecting with Server"""
    def connectServer(self):
        # Socket for receiving arbitrary input
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        host = (self.host, self.port)
        self.sock.connect(host)

    """ Sending File Data to Server"""
    def sendFile(self):
        fileobj = open(self.filename,'r')
        filedata = fileobj.read()
        # Converting file data into String
        DATA = dumps(filedata)
        self.sock.send(DATA)
        fileobj.close()
        self.sock.close()

    """ Receiving File Data from Server"""
    def recvFile(self):
        fileobj = open("recv.txt","w")
        DATA = ""
        # Receiving Arbitrary Data from Server
        while True:
            data = self.sock.recv(BUFSIZE)
            if not data:
                break
            DATA += data
        # Converting received data into original data
        filedata = loads(DATA)
        # Writing Received Data to File and closing it
        fileobj.write(filedata)
        fileobj.close()
        self.sock.close()
    
if __name__ == '__main__':
    # Parsing the Command Line Arguments
    args = parser.parse_args()
    host = args.host
    filename = ""
    if args.recv:
        opt = "recv"
    else:
        opt = "send"
        filename = args.send

    # Making Client Object
    client = Client(host, opt, filename)

    if opt == "recv":
        client.recvFile()
    else:
        client.sendFile()
