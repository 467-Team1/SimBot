import socket
import time

# Raspberry Pi IP address and port
server_ip = 'localhost'  # Listen on localhost
server_port = 12345  # Choose a port that is not already in use

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()

print("Connected to:", client_address)

try:
    # Open file in append mode
    with open("left_hand_label.txt", "a") as file:
        latest_data = None  # Variable to store the latest received data
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # If no data is received, exit the loop
            
            # Store the latest received data
            latest_data = data
            
            # Wait for 2 seconds before processing and receiving more data
            time.sleep(2)
            
            if latest_data is not None:
                # Write the most recent data to the file
                file.write(latest_data + '\n')
                # Process the most recent data (example: print it)
                print("Received data:", latest_data)
                print("Result:", latest_data)
                # Clear the latest_data variable
                latest_data = None

finally:
    # Close the connection
    client_socket.close()
    server_socket.close()
