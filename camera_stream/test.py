import lcm
import numpy as np
import time
import sys
import os
from enum import Enum
import socket

def main():

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

    while True:
        # Exit Condition if Ctrl+C is 
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            print("Received data:", data)
        except:
            print("Data not received...")
            sys.exit()

if __name__ == '__main__':
    main()