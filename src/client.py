import socket

# Define host and port
host = 'Raspberry Pi IP address'  # Raspberry Pi IP address
port = 12345  # Same port number as the server

# Create socket object
client_socketDC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socketSTPR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
client_socketDC.connect((host, port))
# client_socketSTPR.connect((host, port))

while True:
    # Get user input
    message1 = input('Enter message (maju/mundur/kiri/kanan/stop : kecepatan): ')
   
    # Send data to server
    client_socketDC.sendall(message1.encode())
    
    if message1 == 'exit':
        break

# Close connection
client_socketDC.close()
