# TCP client side

import socket

#create a client sode ipv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to a server located at given ip and port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

#recieve a message form the server...must specify the max number of bytes
message = client_socket.recv(1024)
print(message.decode('utf-8'))
#print(type(message))

#close the client socket
client_socket.close()
