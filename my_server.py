import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 55555
ENCODE = "utf-8"
BYTE_SIZE = 64

my_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_server_socket.bind((HOST, PORT))

my_server_socket.listen()

other_socket, other_addr = my_server_socket.accept()

while True:
    message = other_socket.recv(BYTE_SIZE).decode(ENCODE)
    if message == 'quit':
        print('Server disconnected!')
        break
    else:
        print(f'\n{message}') 
        