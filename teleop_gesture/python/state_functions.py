from enum import Enum
import numpy as np
import pygame

class State(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    STAND_BY = 5

# Slow Down - decelerates to 0.05 m/s, 0.05 rad/s or -0.05 m/s, -0.05 rad/s
def slow_down(cur_motor_command, current_state):
    step = 0.05
    print("Decelerating...")
    # Decrease the speed until it reaches 0.05 m/s
    if current_state == State.FORWARD:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v <= 0.05:
            cur_motor_command.trans_v = 0.05

        cur_motor_command.trans_v -= step

    # Increase the speed until it reaches -0.05 m/s
    elif current_state == State.BACKWARD:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v <= -0.05:
            cur_motor_command.trans_v = -0.05

        cur_motor_command.trans_v += step

    # Decrease the angular velocity until it reaches 0.05 rad/s
    elif current_state == State.LEFT:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.angular_v <= 0.05:
            cur_motor_command.angular_v = 0.05

        cur_motor_command.angular_v -= step

    # Increase the angular velocity until it reaches -0.05 rad/s
    elif current_state == State.RIGHT:   
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.angular_v <= -0.05:
            cur_motor_command.angular_v = -0.05

        cur_motor_command.angular_v += step

# Speed Up - accelerates to 0.5 m/s, 1.0 rad/s or -0.5 m/s, -1.0 rad/s
def speed_up(cur_motor_command, current_state):
    step = 0.05
    print("Accelerating...")
    # Increase the speed until it reaches 0.5 m/s
    if current_state == State.FORWARD:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v >= 0.5:
            cur_motor_command.trans_v = 0.5

        cur_motor_command.trans_v += step

    # Increase the speed until it reaches -0.5 m/s
    elif current_state == State.BACKWARD:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v <= -0.5:
            cur_motor_command.trans_v = -0.5
            

        cur_motor_command.trans_v -= step

    # Increase the angular velocity until it reaches 1.0 rad/s
    elif current_state == State.LEFT:
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.angular_v >= 1.0:
            cur_motor_command.angular_v = 1.0
            

        cur_motor_command.angular_v += step

    # Increase the angular velocity until it reaches -0.05 rad/s
    elif current_state == State.RIGHT:   
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.angular_v <= -1.0:
            cur_motor_command.angular_v = -1.0
            

        cur_motor_command.angular_v -= step

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

# Going Forward - climbs up to 0.25 m/s or stays at 0.25 m/s
def forward(cur_motor_command, key_input): #, left_hand_gesture):

    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if key_input[pygame.K_w]: #left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.FORWARD)
    if key_input[pygame.K_s]: #left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.FORWARD)
    if key_input[pygame.K_SPACE]: #left_hand_gesture == "Stop":
        stop(cur_motor_command, State.FORWARD)
    else:
        # Check if the robot is already moving forward
        if cur_motor_command.trans_v >= 0.0:
            return State.FORWARD

        # Slowly Accelrate to 0.25 m/s - Change '10' to '>10' to control the speed of acceleration
        for step in np.linspace(0, 0.25, 10):
            cur_motor_command.trans_v += step

# Going Backward - climbs down to -0.25 m/s or stays at -0.25 m/s
def backward(cur_motor_command, key_input): #, left_hand_gesture

    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if key_input[pygame.K_w]: #left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.BACKWARD)
    if key_input[pygame.K_s]: #left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.BACKWARD)
    if key_input[pygame.K_SPACE]: #left_hand_gesture == "Stop":
        stop(cur_motor_command, State.BACKWARD)
    else:
        # Check if the robot is already moving backward
        if cur_motor_command.trans_v <= 0.0:
            return State.BACKWARD
        
        # Slowly Decelerate to -0.25 m/s - Change '10' to '>10' to control the speed of deceleration
        for step in np.linspace(0, 0.25, 10):
            cur_motor_command.trans_v -= step

# Going Left - turns left at 0.5 rad/s
def left(cur_motor_command, key_input): #, left_hand_gesture
    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if key_input[pygame.K_w]: #left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.LEFT)
    if key_input[pygame.K_s]: #left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.LEFT)
    if key_input[pygame.K_SPACE]: #left_hand_gesture == "Stop":
        stop(cur_motor_command, State.LEFT)
    else:
        # Check if the robot is already turning left
        if cur_motor_command.angular_v >= 0.0:
            return State.LEFT

        # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
        for step in np.linspace(0, 0.5, 10):
            cur_motor_command.angular_v += step

# Going Right - turns right at -0.5 rad/s
def right(cur_motor_command, key_input): #, left_hand_gesture
    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if key_input[pygame.K_w]: #left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.RIGHT)
    if key_input[pygame.K_s]: #left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.RIGHT)
    if key_input[pygame.K_SPACE]: #left_hand_gesture == "Stop":
        stop(cur_motor_command, State.RIGHT)
    else:
        # Check if the robot is already turning right
        if cur_motor_command.angular_v <= 0.0:
            return State.RIGHT

        # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
        for step in np.linspace(0, 0.5, 10):
            cur_motor_command.angular_v -= step