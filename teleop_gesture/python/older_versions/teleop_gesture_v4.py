# Packages
import lcm
from lcmtypes import mbot_motor_command_t
import time
import sys
import RPi.GPIO as GPIO
from state_functions import *
import socket
import os

def main():

    # --- --- Claw initialization Start --- --- 

    # Claw check - begins at false since claw is open
    Claw_is_Closed = False

    # Needed to avoid GPIO warnings
    GPIO.setwarnings(False)

    # We need to name all of the pins, so set the naming mode 
    # as this sets the names to board mode, which just names the pins 
    # according to the numbers
    GPIO.setmode(GPIO.BOARD)

    # we need an output to send our PWM signal on
    # NOTE: Pin 11 is the GPIO pin and it can be changed
    GPIO.setup(11, GPIO.OUT)

    # setup PWM at 400 Hz
    # The freq is unique to the servo motor
    pwm = GPIO.PWM(11, 400)
    pwm.start(25)

    # --- --- Claw initialization End --- --- 

    # --- --- Socket initialization Start --- --- 

    # Raspberry Pi IP address and port
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    # TODO: Replace host IP with MBot's if MBot IP changed (use ifconfig and use the wlan0 IP address)
    server_ip = '192.168.1.3'  # Listen on localhost
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

    # --- --- Socket initialization End --- --- 

    # Default settings are Stop and Forward
    left_hand_gesture= "Stop"
    right_hand_gesture = "Forward"

    #  --- --- Clear data.txt so no remaining values exist --- --- 
    with open('data.txt','w'):
        pass
    
     #  --- --- FLIPPER for alternating angle correction and distance --- --- 
    angle_distance_flipper = True

    # ------------------------------------------------------------

    # LCM Object
    lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")
    time.sleep(0.5)

    # State Machine - Our initial state is always StandBy
    current_state = State.STAND_BY

    # Initialize the motor command
    cur_motor_command = mbot_motor_command_t()

    while True:
        # Exit Condition if Ctrl+C is pressed
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            # print("Received data:", data)
            if data == "Continue" or data == "Stop" or data == "SpeedUp" or data == "SlowDown":
                left_hand_gesture = data
            elif data == "Forward" or data == "Backwards" or data == "TurnRight" or data == "TurnLeft" or data == "Open" or data == "Close":
                right_hand_gesture = data
            else:
                None

            print("Current Left gesture: ", left_hand_gesture)
            print("Current Right gesture: ", right_hand_gesture)

        except:
            print("Data not received...")
            sys.exit()

        # --- --- State Machine --- --- 
        print("CURRENT STATE: ", current_state)
        # --- --- Autonomous --- --- 

        # Check if the data.txt file is not empty a.k.a April Tag has been clicked on
        if os.stat("data.txt").st_size != 0:
            ### WHEN IN AUTO PLEASE BLINK YOUR LEFT HAND IN GESTURE CAMERA ###
            print("AUTO MODE ON")
            current_state = State.AUTO
        
        else:
            # Open and Close call after going to April Tagged obstacle
            current_state = claw_open(cur_motor_command, pwm)
            current_state = claw_close(cur_motor_command, pwm)
            current_state = State.STAND_BY

        # Enter AUTO state
        if current_state == State.AUTO:
            with open('data.txt','r') as file:
                # Collect all 3 variables
                for line in file:
                    variables = line.strip().split()
        
                if len(variables) < 1:
                    return State.AUTO
            
            # Angle will always be sent and collected
            angle = float(variables[0])
            
            if (len(variables) > 3):
                # angle, dis, id, log
                # distance = float(variables[1])
                # tag_id = int(id)
                print("in double click")
                current_state = angle_alignment(cur_motor_command, angle)
                
            else:
                distance = float(variables[1])
                
                # Run the entire autonomous part of picking up the object
                # We will only be at this point if we have clicked on an april tag
                if angle_distance_flipper:
                    current_state = angle_alignment(cur_motor_command, angle, distance)
                    angle_distance_flipper = False
                else:   
                    current_state = distance_alignment(cur_motor_command, distance)
                    angle_distance_flipper = True

        # --- --- Right Hand --- --- 

        if right_hand_gesture == "Forward" and current_state != State.AUTO:
            current_state = forward(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        elif right_hand_gesture == "Backwards" and current_state != State.AUTO:
            current_state = backward(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        elif right_hand_gesture == "TurnLeft" and current_state != State.AUTO:
            current_state = left(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        elif right_hand_gesture == "TurnRight" and current_state != State.AUTO:
            current_state = right(cur_motor_command, left_hand_gesture)
            print("State: ", current_state)

        # --- --- Claw --- --- 

        elif right_hand_gesture == "Close" and Claw_is_Closed == False and current_state != State.AUTO:
            current_state = claw_close(cur_motor_command, pwm)
            print("State: ", current_state)

            # Update the claw flag
            Claw_is_Closed = True
        
        elif right_hand_gesture == "Open" and Claw_is_Closed == True and current_state != State.AUTO:
            current_state = claw_open(cur_motor_command, pwm)
            print("State: ", current_state)

            # Update the claw flag
            Claw_is_Closed = False

        # --- --- End of State Machine --- --- 

        # Publish the current motor command
        lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

        # Sleep for 0.1 seconds
        time.sleep(0.1)
    

if __name__ == '__main__':
    main()
