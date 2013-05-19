from server import Server
from client import Client
from thread import *
import unittest

""" Starting Server """
class TestServer(object):
    def __init__(self):
        self.testServer = Server()
        # Starting Receiving & Sending Function from server.py
        start_new_thread(self.testServer.recvClient, ())
        start_new_thread(self.testServer.sendClient, ())
        start_new_thread(self.testServer.wait, ())

""" Testing Sending and Receiving Clients """
class TestClient(unittest.TestCase):
    def setUp(self):
        # Staring Server by making TestServer class object
        self.test = TestServer()
        
    def test_send_client(self):
        self.opt = "send"
        self.host = "localhost"
        self.filename = "testdata.txt"
        # Starting Data Sending Client        
        self.sendClient = Client(self.host, self.opt, self.filename)
        start_new_thread(self.sendClient.sendFile,())
    
    def test_recv_client(self):
        self.opt = "recv"
        self.host = "localhost"
        self.filename = ""
        # Starting Client Receiving Data
        self.recvClient = Client(self.host, self.opt, self.filename)
        start_new_thread(self.recvClient.recvFile, ())

if __name__ == "__main__":
    unittest.main()
