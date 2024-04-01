import lcm
import numpy as np
import pygame
from lcmtypes import mbot_motor_command_t
from lcmtypes import mbot_encoder_t
import time
import sys
import os
from enum import Enum

class State(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    STOP = 5
    ACCELERATE = 6
    DECELERATE = 7

# Going Forward - climbs up to 0.25 m/s or stays at 0.25 m/s
def forward(cur_motor_command):
    # Check if the robot is already moving forward
    if cur_motor_command.trans_v >= 0.0:
        return State.FORWARD

    # Slowly Accelrate to 0.25 m/s - Change '10' to '>10' to control the speed of acceleration
    for step in np.linspace(0, 0.25, 10):
        cur_motor_command.trans_v += step

# Going Backward - climbs down to -0.25 m/s or stays at -0.25 m/s
def backward(cur_motor_command):
    # Check if the robot is already moving backward
    if cur_motor_command.trans_v <= 0.0:
        return State.BACKWARD
    
    # Slowly Decelerate to -0.25 m/s - Change '10' to '>10' to control the speed of deceleration
    for step in np.linspace(0, 0.25, 10):
        cur_motor_command.trans_v -= step

# Going Left - turns left at 0.5 rad/s
def left(cur_motor_command):
    # Check if the robot is already turning left
    if cur_motor_command.angular_v >= 0.0:
        return State.LEFT

    # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
    for step in np.linspace(0, 0.5, 10):
        cur_motor_command.angular_v += step

# Going Right - turns right at -0.5 rad/s
def right(cur_motor_command):
    # Check if the robot is already turning right
    if cur_motor_command.angular_v <= 0.0:
        return State.RIGHT

    # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
    for step in np.linspace(0, 0.5, 10):
        cur_motor_command.angular_v -= step

# Slow Down - decelerates to 0.05 m/s, 0.05 rad/s or -0.05 m/s, -0.05 rad/s
def slow_down(cur_motor_command, current_state, parent_state):
    step = 0.05
    while current_state == State.DECELERATE:
        print("Decelerating...")
        # Decrease the speed until it reaches 0.05 m/s
        if parent_state == State.FORWARD:
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.trans_v <= 0.05:
                cur_motor_command.trans_v = 0.05
                continue

            cur_motor_command.trans_v -= step

        # Increase the speed until it reaches -0.05 m/s
        elif parent_state == State.BACKWARD:
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.trans_v <= -0.05:
                cur_motor_command.trans_v = -0.05
                continue

            cur_motor_command.trans_v += step

        # Decrease the angular velocity until it reaches 0.05 rad/s
        elif parent_state == State.LEFT:
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.angular_v <= 0.05:
                cur_motor_command.angular_v = 0.05
                continue

            cur_motor_command.angular_v -= step

        # Increase the angular velocity until it reaches -0.05 rad/s
        elif parent_state == State.RIGHT:   
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.angular_v <= -0.05:
                cur_motor_command.angular_v = -0.05
                continue

            cur_motor_command.angular_v += step

    return parent_state

# Speed Up - accelerates to 0.5 m/s, 1.0 rad/s or -0.5 m/s, -1.0 rad/s
def speed_up(cur_motor_command, current_state, parent_state):
    step = 0.05
    while current_state == State.ACCELERATE:
        print("Accelerating...")
        # Increase the speed until it reaches 0.5 m/s
        if parent_state == State.FORWARD:
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.trans_v >= 0.5:
                cur_motor_command.trans_v = 0.5
                continue

            cur_motor_command.trans_v += step

        # Increase the speed until it reaches -0.5 m/s
        elif parent_state == State.BACKWARD:
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.trans_v <= -0.5:
                cur_motor_command.trans_v = -0.5
                continue

            cur_motor_command.trans_v -= step

        # Increase the angular velocity until it reaches 1.0 rad/s
        elif parent_state == State.LEFT:
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.angular_v >= 1.0:
                cur_motor_command.angular_v = 1.0
                continue

            cur_motor_command.angular_v += step

        # Increase the angular velocity until it reaches -0.05 rad/s
        elif parent_state == State.RIGHT:   
            # Check if the robot is the robot reached the minimum speed
            if cur_motor_command.angular_v <= -1.0:
                cur_motor_command.angular_v = -1.0
                continue

            cur_motor_command.angular_v -= step

    return parent_state

# Stop - decelerates to 0.0 m/s, 0.0 rad/s
def stop(cur_motor_command, current_state):
    step = 0.05
    if current_state == State.FORWARD:
        while cur_motor_command.trans_v > 0:
            cur_motor_command.trans_v -= step

    elif current_state == State.BACKWARD:
        while cur_motor_command.trans_v < 0:
            cur_motor_command.trans_v += step

    elif current_state == State.LEFT:
        while cur_motor_command.angular_v > 0:
            cur_motor_command.angular_v -= step

    elif current_state == State.RIGHT:
        while cur_motor_command.angular_v < 0:
            cur_motor_command.angular_v += step

    return State.STOP

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
            # pass
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


