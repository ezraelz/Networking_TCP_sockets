# TCP server side

import socket 

# create a server side socket using ipv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# dynamic ip address
# print(socket.gethostname()) # host name
# print(socket.gethostbyname(socket.gethostname())) # if of host name

#bind our new socket
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

#put the socket into listening mode to any possible connections
server_socket.listen()

#listen forever to accept any connection
while True:
    #accept every single connection and store two pieces of info
    client_socket, client_address = server_socket.accept()
    #print(type(client_socket))
    print(client_socket)
    #print(type(client_address))
    #print(client_address)

    print(f"[CONNECTED TO: ] {client_address}")

    #send a message to the client that just connected
    client_socket.send("You are connected!".encode('utf-8'))

    #close the connection
    server_socket.close()
    break
