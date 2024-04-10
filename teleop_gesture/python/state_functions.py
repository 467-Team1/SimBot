from enum import Enum
import numpy as np
import pygame
import time

class State(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    STAND_BY = 5

# Slow Down - decelerates to 0.05 m/s, 0.05 rad/s or -0.05 m/s, -0.05 rad/s
def slow_down(lc, cur_motor_command, current_state):
    step = 0.02
    trans_speed_cap = 0.30
    angul_speed_cap = 1.0

    print("Deccelerating... current state is: ", current_state)
    print("Current speed is: ", cur_motor_command.trans_v)
    time.sleep(2)
    # Decrease the speed until it reaches 0.05 m/s
    if current_state == State.FORWARD and cur_motor_command.trans_v > trans_speed_cap:
        # Check if the robot is the robot reached the minimum speed
        time.sleep(1)
        print("Currently speeding forward... Velocity is: ", cur_motor_command.trans_v)
        cur_motor_command.trans_v -= step

    # Increase the speed until it reaches -0.05 m/s
    elif current_state == State.BACKWARD:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v <= -1*trans_speed_cap:
            cur_motor_command.trans_v = -1*trans_speed_cap

        cur_motor_command.trans_v = step

    # Decrease the angular velocity until it reaches 0.05 rad/s
    elif current_state == State.LEFT:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.angular_v <= angul_speed_cap:
            cur_motor_command.angular_v = angul_speed_cap

        cur_motor_command.angular_v = -step

    # Increase the angular velocity until it reaches -0.05 rad/s
    elif current_state == State.RIGHT:   
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.angular_v <= -1*angul_speed_cap:
            cur_motor_command.angular_v = -1*angul_speed_cap

        cur_motor_command.angular_v = step

# Speed Up - accelerates to 0.5 m/s, 1.0 rad/s or -0.5 m/s, -1.0 rad/s
def speed_up(lc, cur_motor_command, current_state):
    step = 0.02
    trans_speed_cap = 0.40
    angul_speed_cap = 1.0
    # print("Initial key_input: ", key_input)
    print("Accelerating... current state is: ", current_state)
    print("Current speed is: ", cur_motor_command.trans_v)
    time.sleep(2)

    # Increase the speed until it reaches 0.5 m/s
    if current_state == State.FORWARD and cur_motor_command.trans_v < trans_speed_cap:
        # Check if the robot is the robot reached the minimum speed
        time.sleep(1)
        print("Currently speeding forward... Velocity is: ", cur_motor_command.trans_v)
        cur_motor_command.trans_v += step

    # Increase the speed until it reaches -0.5 m/s
    elif current_state == State.BACKWARD and cur_motor_command.trans_v > -trans_speed_cap:
        # Check if the robot is the robot reached the minimum speed
        time.sleep(1)
        print("Currently speeding backward... Velocity is: ", cur_motor_command.trans_v)
        cur_motor_command.trans_v -= step

    # Increase the angular velocity until it reaches 1.0 rad/s
    elif current_state == State.LEFT and cur_motor_command.angular_v < angul_speed_cap:
        # Check if the robot is the robot reached the minimum speed
        time.sleep(1)
        print("Currently speeding left... Velocity is: ", cur_motor_command.angular_v)
        cur_motor_command.angular_v += step

    # Increase the angular velocity until it reaches -0.05 rad/s
    elif current_state == State.RIGHT and cur_motor_command.angular_v > -angul_speed_cap:   
        # Check if the robot is the robot reached the minimum speed=
        time.sleep(1)
        print("Currently speeding right... Velocity is: ", cur_motor_command.angular_v)
        cur_motor_command.angular_v -= step

    # lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())
    return current_state

# Stop - decelerates to 0.0 m/s, 0.0 rad/s
def stop(lc, cur_motor_command, current_state):
    step = 0.1
    cur_motor_command.trans_v = 0.0
    cur_motor_command.angular_v = 0.0
    if current_state == State.FORWARD:
        while cur_motor_command.trans_v > 0:
            time.sleep(1)
            print("Currently stopping forward... Velocity is: ", cur_motor_command.angular_v)
            cur_motor_command.trans_v -= step
            lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

    elif current_state == State.BACKWARD:
        while cur_motor_command.trans_v < 0:
            time.sleep(1)
            print("Currently stopping backward... Velocity is: ", cur_motor_command.angular_v)
            cur_motor_command.trans_v += step
            lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

    elif current_state == State.LEFT:
        while cur_motor_command.angular_v > 0:
            time.sleep(1)
            print("Currently stopping left... Velocity is: ", cur_motor_command.angular_v)
            cur_motor_command.angular_v -= step
            lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())

    elif current_state == State.RIGHT:
        while cur_motor_command.angular_v < 0:
            time.sleep(1)
            print("Currently stopping right... Velocity is: ", cur_motor_command.angular_v)
            cur_motor_command.angular_v += step
            lc.publish("MBOT_MOTOR_COMMAND", cur_motor_command.encode())
    
    return State.STAND_BY

# Going Forward - climbs up to 0.25 m/s or stays at 0.25 m/s
def forward(cur_motor_command): #, left_hand_gesture):
    
    # Zero Out Angular Velocity
    cur_motor_command.angular_v = 0.0

    # Check if the robot is already moving forward
    if cur_motor_command.trans_v > 0.0:
        return State.FORWARD

    # Slowly Accelrate to 0.25 m/s - Change '10' to '>10' to control the speed of acceleration
    for step in np.linspace(0, 0.25, 10):
        print("Getting to Speed...")
        cur_motor_command.trans_v = step
    
    return State.FORWARD

# Going Backward - climbs down to -0.25 m/s or stays at -0.25 m/s
def backward(cur_motor_command): #, left_hand_gesture
     
    # Zero Out Angular Velocity
    cur_motor_command.angular_v = 0.0

    # Check if the robot is already moving backward
    if cur_motor_command.trans_v < 0.0:
        return State.BACKWARD
    
    # Slowly Decelerate to -0.25 m/s - Change '10' to '>10' to control the speed of deceleration
    for step in np.linspace(0, 0.25, 10):
        cur_motor_command.trans_v = -step

    return State.BACKWARD

# Going Left - turns left at 0.5 rad/s
def left(cur_motor_command): #, left_hand_gesture

    # Zero out Trans Velocity
    cur_motor_command.trans_v = 0.0

    # Check if the robot is already turning left
    if cur_motor_command.angular_v > 0.0:
        return State.LEFT

    # if the robot is not currently going left, it may be going left
    # therefore we must zero the angular velocity before turning directions
    cur_motor_command.angular_v = 0.0

    # Slowly Accelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
    for step in np.linspace(0, 0.5, 10):
        cur_motor_command.angular_v += step

    return State.LEFT

# Going Right - turns right at -0.5 rad/s
def right(cur_motor_command): #, left_hand_gesture

    # Zero out Trans Velocity
    cur_motor_command.trans_v = 0.0

    # Check if the robot is already turning right
    if cur_motor_command.angular_v < 0.0:
        return State.RIGHT

    # if the robot is not currently going right, it may be going left
    # therefore we must zero the angular velocity before turning directions
    cur_motor_command.angular_v = 0.0

    # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
    for step in np.linspace(0, 0.5, 10):
        cur_motor_command.angular_v -= step

    return State.RIGHT