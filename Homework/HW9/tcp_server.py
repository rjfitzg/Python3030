'''
Homework 9 Exercise 2
Riley Fitzgibbons
4/30/19
Base code from: https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
'''

import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on %s, %S', (bind_ip, bind_port))


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    if request not in range(1,4):
        # If options not in request, send options
        client_socket.send(b'1: Read Str \n2: Change Str \n3:Quit')
    elif(request == '1'):
        # Send serv_str if requested 
        client_socket.send(serverStr)
    elif ('2' in request):
        # Change serv_str as requested
        serv_str = request
        client_socket.send(serverStr)
    elif ('3' == request)
        import sys
        sys.exit(0)

while True:
    client_sock, address = server.accept()
    print('Accepted connection from %s:%s', (address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()