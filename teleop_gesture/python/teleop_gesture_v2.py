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

def main():

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

    # Open the gesture files
    left_hand_file = open("../../hand-gesture-recognition/left_hand_labels.txt", "r")
    right_hand_file = open("../../hand-gesture-recognition/right_hand_labels.txt", "r")


    while True:
        # Exit Condition if Ctrl+C is 
        try:
            # For Testing Purposes ONLY #
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #############################
            # pass -> Uncomment this line when you are ready to implement gestures
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()
            
        key_input = pygame.key.get_pressed() 

        # Read the first line from the left hand & right hand files - used to change the state
        left_hand_gesture = left_hand_file.readline().strip()
        right_hand_gesture = right_hand_file.readline().strip()

        # State Machine
        if key_input[pygame.K_UP]: # if right_hand_gesture == "Forward":
            current_state = forward(cur_motor_command, key_input) #left_hand_gesture)
            print("State: ", current_state)

        elif key_input[pygame.K_DOWN]: # if right_hand_gesture == "Backwards":
            current_state = backward(cur_motor_command, key_input) #left_hand_gesture)
            print("State: ", current_state)

        elif key_input[pygame.K_LEFT]: # if right_hand_gesture == "TurnLeft":
            current_state = left(cur_motor_command, key_input) #left_hand_gesture)
            print("State: ", current_state)

        elif key_input[pygame.K_RIGHT]: # if right_hand_gesture == "TurnRight":
            current_state = right(cur_motor_command, key_input) #left_hand_gesture)
            print("State: ", current_state)

        # Publish the motor command - [might be worth having cur_motor_command published every single time it changes
        # not sure if this will slow down computation, more than likely, for now just leave it here until further testing]
        lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

        # Sleep for 0.1 seconds
        time.sleep(0.1)

if __name__ == '__main__':
    main()


