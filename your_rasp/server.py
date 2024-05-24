# import socket
# from motion import set_motor
# import RPi.GPIO as GPIO

# # Define host and port
# host = '0.0.0.0'  # Raspberry Pi IP address
# port = 12345  # Arbitrary port number

# # Create socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind socket to address and port
# server_socket.bind((host, port))

# # Listen for incoming connections
# server_socket.listen(1)

# print('Waiting for connection...')

# # Accept connection
# client_socket, client_address = server_socket.accept()
# print(f'Connection from {client_address}')

# def start_server():
#     # Define host and port
#     host = '0.0.0.0'  # Raspberry Pi IP address
#     port = 12345  # Arbitrary port number

#     # Create socket object
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Bind socket to address and port
#     server_socket.bind((host, port))

#     # Listen for incoming connections
#     server_socket.listen(1)

#     print('Waiting for connection...')

#     # Accept connection
#     client_socket, client_address = server_socket.accept()
#     print(f'Connection from {client_address}')
#     try:
#         while True:
#             # Receive data from client
#             data = client_socket.recv(1024).decode()
            
#             if not data:
#                 break
            
#             print(f'Received: {data}')
            
#             # Process received data (e.g., control motors)
#             parts = data.split(':')
#             if len(parts)==2:
#                 direct = parts[0]
#                 try :
#                     speed = int(parts[1])
#                     set_motor(speed, direct)
#                 except ValueError:
#                     print("invalid nilai kecepatan")
#             else:
#                 print("invalid format gerak robot")

#     except KeyboardInterrupt:
#         print("Server keluar.")
#     finally:
#     # Close connection
#         client_socket.close()
#         server_socket.close()
#         GPIO.cleanup()

# if __name__ =="__main__":
#     start_server()

