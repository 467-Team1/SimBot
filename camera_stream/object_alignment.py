'''
This program should run after an april tag has been clicked on

Step 1: The robot will receive the data of the pose of the april tag once selected.
Step 2: Using the pose received from the april tag, the robot calculate the angle between itself and the center of the april tag.
Step 3: The robot will turn to face the april tag (until the z value is 0).
Step 4: The robot will move forward until the april tag is at a distance of 10 mm (threshold needs to be tested).
Step 5: The robot will open and close the claw.
Step 6: The robot will switch back to the teleop code.

'''
import numpy as np
from lcmtypes import mbot_motor_command_t
from lcmtypes import mbot_encoder_t

from flask import Flask, request, jsonify
app = Flask(__name__)

# Assuming the pose of the april tag is being collected from the april tag
tag_pose = np.array([[0.8835, -0.4682, -0.0133, 0.0163], [0.4682, 0.8820, 0.0532, 0.0054], [-0.0131, -0.0532, 0.9985, 0.1433], [0.0000, 0.0000, 0.0000, 1.0000]])

# Flag of whether the bot is close enough to tag, assumed that we are getting it
is_tag_head_on = False

# Collect Pose of the April Tag
def receive_data():
    return

def yaw_angle(R):
    # Convert the rotation matrix to euler angles
    beta = -np.arcsin(R[2,0]) # equivalent to y axis
    return np.arctan2(R[1,0]/np.cos(beta), R[0,0]/np.cos(beta)) # equivalent to z axis

def angle_correction(cur_motor_command):
    
    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0

    # Turn the robot until the z value ~0
    while yaw_angle(tag_pose[0:3, 0:3]) > 0.15 or yaw_angle(tag_pose[0:3, 0:3]) < -0.15:
        if yaw_angle(tag_pose[0:3, 0:3]) > 0.15:
            cur_motor_command.angular_v = 0.1
        elif yaw_angle(tag_pose[0:3, 0:3]) < -0.15:
            cur_motor_command.angular_v = -0.1

    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0
    
    return

def distance_correction(cur_motor_command):
    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    while not is_tag_head_on:
        # Move the robot forward until the tag is head on
        cur_motor_command.trans_v = 0.1

    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    return
