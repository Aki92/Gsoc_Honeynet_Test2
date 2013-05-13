Gsoc_Honeynet_Test2
==================
A Client Server Program where a client sends arbitrary data to Server on one Socket and then Server forwards that data to another client connected on other Socket.


SERVER:
It receives arbitrary data from Client1 and forwards same data to Client2.  
Files: server.py    
Usage: python server.py

CLIENT1:
It sends arbitrary data to server.    
Files: client1.py    
Usage: python client1.py server_address

CLIENT2:
It receives arbitrary data from Server.   
Files: client2.py   
usage: python client2.py server_address

config.py:
It stores all Variables used in other codes.

Example:    
Steps to Run single Client-Server functioning:

$ python server.py    
$ python client1.py 127.0.0.1    
$ python client2.py 127.0.0.1


(If command line argument is not given then it would take 127.0.0.1 by default)
