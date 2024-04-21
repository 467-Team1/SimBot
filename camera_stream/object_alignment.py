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
angle = None

# Flag of whether the bot is close enough to tag, assumed that we are getting it
head_on = None

# Collect Pose of the April Tag
@app.route('/', methods=['POST'])
def receive_data():
    global angle
    global head_on
    data = request.json

    if data.get('status') == 'DONE':
        print('DONE TRACKING TAG')
    else:
        # Assuming the data includes 'corners' and 'distance' as sent by your application
        angle = data.get('angle')
        head_on = data.get('headon')
    
    # Return a success response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(host='0.0.0.0', port=5003, debug=True)

def angle_correction(cur_motor_command):
    
    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0

    # Turn the robot until the z value ~0
    while angle > 0.15 or angle < -0.15:
        if angle > 0.15:
            cur_motor_command.angular_v = 0.1
        elif angle < -0.15:
            cur_motor_command.angular_v = -0.1

    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0
    
    return

def distance_correction(cur_motor_command):
    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    while not head_on:
        # Move the robot forward until the tag is head on
        cur_motor_command.trans_v = 0.1

    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    return

def test():
    global angle
    global head_on
    print("Angle" + angle)
    print("Head On" + head_on)

# Main
if __name__ == '__main__':
    # Test the functions
    test()

