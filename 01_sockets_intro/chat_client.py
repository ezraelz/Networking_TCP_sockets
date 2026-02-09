import socket

# Define the constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTSIZE = 1024

# Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


# Send/Recieve messages
while True:
    # Recieve information from the server
    message = client_socket.recv(BYTSIZE).decode(ENCODER)

    # Quit if the connected server wants to quit
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat....goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))


client_socket.close()