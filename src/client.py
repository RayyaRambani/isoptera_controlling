import socket

# Define host and port
host = 'Raspberry Pi IP address'  # Raspberry Pi IP address
port = 12345  # Same port number as the server

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((host, port))

while True:
    # Get user input
    message = input('Enter message (maju/mundur/kiri/kanan/stop : kecepatan): ')
    
    # Send data to server
    client_socket.sendall(message.encode())
    
    if message == 'exit':
        break

# Close connection
client_socket.close()
