import lcm
import numpy as np
import pygame
from lcmtypes import mbot_motor_command_t
from lcmtypes import mbot_encoder_t
import time
import sys
import os
from enum import Enum
from state_functions import *
import socket
from flask import Flask, request, jsonify


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

    left_hand_gesture= "Stop"
    right_hand_gesture = "Forward"

    # ------------------------------------------------------------

    # LCM Object
    lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

    # For Testing Purposes ONLY #
    pygame.init()
    pygame.display.set_caption("MBot TeleOp")
    screen = pygame.display.set_mode([100,100])
    ###########################################

    time.sleep(0.5)

    # State Machine
    current_state = State.STAND_BY

    # Initialize the motor command
    cur_motor_command = mbot_motor_command_t()

    while True:
        # Exit Condition if Ctrl+C is 
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            # print("Received data:", data)
            if data == "Continue" or data == "Stop" or data == "SpeedUp" or data == "SlowDown":
                left_hand_gesture = data
            elif data == "Forward" or data == "Backwards" or data == "TurnRight" or data == "TurnLeft":
                right_hand_gesture = data
            else:
                None
            print("Left gesture: ", left_hand_gesture)
            print("Right gesture: ", right_hand_gesture)

        except:
            print("Data not received...")
            sys.exit()

        # State Machine
        if right_hand_gesture == "Forward":
            current_state = forward(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        elif right_hand_gesture == "Backwards":
            current_state = backward(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        elif right_hand_gesture == "TurnLeft":
            current_state = left(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        elif right_hand_gesture == "TurnRight":
            current_state = right(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        # Publish the motor command - [might be worth having cur_motor_command published every single time it changes
        # not sure if this will slow down computation, more than likely, for now just leave it here until further testing]
        lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

        # Sleep for 0.1 seconds
        time.sleep(0.1)

if __name__ == '__main__':
    main()