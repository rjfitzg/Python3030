'''
Homework 9 Exercise 2
Riley Fitzgibbons
4/30/19
Create tcp client to communicate with server

Base code from: https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
'''

import socket

hostname, sld, tld, port = 'www', 'integralist', 'co.uk', 80
target = '%s.%s.%s', (hostname, sld, tld)

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('0.0.0.0', 9999))

# Connect and commiunicate to get menu
client.send('hello')

# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)
print(response)

# Check on serv_str
client.send('1')
response = client.recv(4096)
print(response)

# Tell server to change serv_str
client.send('2 new server string')
response = client.recv(4096)
print(response)

# Exit sever 
client.send('2 new server string')


