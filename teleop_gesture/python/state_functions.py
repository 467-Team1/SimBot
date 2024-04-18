from enum import Enum
import numpy as np

class State(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    STAND_BY = 5

### VELOCITY CHANGE FUNCTIONS ### NOT WORKING FULLY YET -> LEAVE AS PRINTS UNTIL MAIN HAS BEEN UPDATED

# Slow Down - decelerates to 0.05 m/s, 0.05 rad/s or -0.05 m/s, -0.05 rad/s
def slow_down(cur_motor_command, current_state):
    step = 0.02
    trans_speed_cap = 0.20

    print("Decelerating...")
    # # Decrease the speed until it reaches 0.05 m/s
    if current_state == State.FORWARD:
        # Check if the robot is the robot reached the minimum speed
        cur_motor_command.trans_v -= step
        if cur_motor_command.trans_v <= trans_speed_cap:
            cur_motor_command.trans_v = trans_speed_cap

    # # Increase the speed until it reaches -0.05 m/s
    elif current_state == State.BACKWARD:
        cur_motor_command.trans_v += step
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v >= -1*trans_speed_cap:
            cur_motor_command.trans_v = -1*trans_speed_cap

# Speed Up - accelerates to 0.5 m/s, 1.0 rad/s or -0.5 m/s, -1.0 rad/s
def speed_up(cur_motor_command, current_state):
    step = 0.02
    trans_speed_cap = 0.40

    print("Accelerating...")
    # # Increase the speed until it reaches 0.5 m/s
    if current_state == State.FORWARD:
        # Check if the robot is the robot reached the minimum speed
        cur_motor_command.trans_v += step
        if cur_motor_command.trans_v >= trans_speed_cap:
            cur_motor_command.trans_v = trans_speed_cap

    # Increase the speed until it reaches -0.5 m/s
    elif current_state == State.BACKWARD:
        cur_motor_command.trans_v -= step
        # Check if the robot is the robot reached the minimum speed
        if cur_motor_command.trans_v <= -1*trans_speed_cap:
            cur_motor_command.trans_v = -1*trans_speed_cap

# Stop - decelerates to 0.0 m/s, 0.0 rad/s
def stop(cur_motor_command):
    print("Stopping...")
    cur_motor_command.trans_v = 0.0

### DIRECTONAL FUNCTIONS ###

# Going Forward - climbs up to 0.25 m/s or stays at 0.25 m/s
def forward(cur_motor_command, left_hand_gesture):
    
    # Zero Out Angular Velocity
    cur_motor_command.angular_v = 0.0

    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.FORWARD)
    if left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.FORWARD)
    if left_hand_gesture == "Stop":
        stop(cur_motor_command, State.FORWARD)
    else:
        # Check if the robot is already moving forward
        if cur_motor_command.trans_v > 0.0:
            return State.FORWARD

        # Slowly Accelrate to 0.25 m/s - Change '10' to '>10' to control the speed of acceleration
        for step in np.linspace(0, 0.25, 10):
            print("Getting to Speed...")
            cur_motor_command.trans_v = step

# Going Backward - climbs down to -0.25 m/s or stays at -0.25 m/s
def backward(cur_motor_command, left_hand_gesture):
     
    # Zero Out Angular Velocity
    cur_motor_command.angular_v = 0.0

    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.BACKWARD)
    if left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.BACKWARD)
    if left_hand_gesture == "Stop":
        stop(cur_motor_command)
    else:
        # Check if the robot is already moving backward
        if cur_motor_command.trans_v < 0.0:
            return State.BACKWARD
        
        # Slowly Decelerate to -0.25 m/s - Change '10' to '>10' to control the speed of deceleration
        for step in np.linspace(0, 0.25, 10):
            cur_motor_command.trans_v = -step

# Going Left - turns left at 0.5 rad/s
def left(cur_motor_command, left_hand_gesture):

    # Zero out Trans Velocity
    cur_motor_command.trans_v = 0.0

    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.LEFT)
    if left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.LEFT)
    if left_hand_gesture == "Stop":
        stop(cur_motor_command)
    else:
        # Check if the robot is already turning left
        if cur_motor_command.angular_v > 0.0:
            return State.LEFT

        # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
        for step in np.linspace(0, 0.5, 10):
            cur_motor_command.angular_v += step

# Going Right - turns right at -0.5 rad/s
def right(cur_motor_command, left_hand_gesture):

    # Zero out Trans Velocity
    cur_motor_command.trans_v = 0.0

    # Check if the left hand gesture is "SpeedUp", "SlowDown", "Continue", or "Stop"
    if left_hand_gesture == "SpeedUp":
        speed_up(cur_motor_command, State.RIGHT)
    if left_hand_gesture == "SlowDown":
        slow_down(cur_motor_command, State.RIGHT)
    if left_hand_gesture == "Stop":
        stop(cur_motor_command)
    else:
        # Check if the robot is already turning right
        if cur_motor_command.angular_v < 0.0:
            return State.RIGHT

        # Slowly Decelerate to 0.0 m/s - Change '10' to '>10' to control the speed of deceleration
        for step in np.linspace(0, 0.5, 10):
            cur_motor_command.angular_v -= step