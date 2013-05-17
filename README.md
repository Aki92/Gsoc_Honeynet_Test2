# **GSoC_Honeynet_Test2**
A Client Server Program where a client sends arbitrary data to Server on one Socket and then Server forwards that data to another client connected on other Socket.


## Server:
It receives arbitrary data from One Client and forwards same data to Other Client.	
Files: server.py    
Usage: ```python server.py```		

## Client:		
It can be used for both Sending Data to server and Receiving Data from Server.
Files: client.py    
Usage: 	```python client1.py --host server_address type(--send filename | --recv)```		
Different Ways of Using client.py:	
```$ python client.py 127.0.0.1 --send data.txt```		
```$ python client.py 127.0.0.1 --recv```		
```$ python client.py --send data.txt```		

## Config:		
It stores all Variables used in other codes.		
Files: config.py		

**Steps to Run Client-Server:**

```$ python server.py```		
```$ python client.py --host 127.0.0.1 --send datafile.txt```		
```$ python client.py --host 127.0.0.1 --recv```		

(**Command for HELP**: 	```python client.py --help```)		

