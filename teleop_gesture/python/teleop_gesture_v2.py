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
    current_state = State.STOP

    # Parent State
    parent_state = State.STOP

    # Initialize the motor command
    cur_motor_command = mbot_motor_command_t()


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

        # State Machine
        if key_input[pygame.K_UP]:
            current_state = forward(cur_motor_command)
            print("State: ", current_state)
            parent_state = State.FORWARD

        elif key_input[pygame.K_DOWN]:
            current_state = backward(cur_motor_command)
            print("State: ", current_state)
            parent_state = State.BACKWARD

        elif key_input[pygame.K_LEFT]:
            current_state = left(cur_motor_command)
            print("State: ", current_state)
            parent_state = State.LEFT

        elif key_input[pygame.K_RIGHT]:
            current_state = right(cur_motor_command)
            print("State: ", current_state)
            parent_state = State.RIGHT

        elif key_input[pygame.K_SPACE]:
            current_state = stop(cur_motor_command, current_state)
            print("State: ", current_state)

        elif key_input[pygame.K_w]:
            print("State: Accelerate")
            current_state = speed_up(cur_motor_command, current_state, parent_state)

        elif key_input[pygame.K_s]:
            print("State: Decelerate")
            current_state = slow_down(cur_motor_command, current_state, parent_state)

        # Publish the motor command
        lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

        # Sleep for 0.1 seconds
        time.sleep(0.1)

if __name__ == '__main__':
    main()


