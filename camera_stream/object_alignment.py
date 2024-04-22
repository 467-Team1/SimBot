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

# Current angle of the robot to the april tag
angle = None

# Current distance of the robot to the april tag
distance = None

# Current motor command
cur_motor_command = mbot_motor_command_t()

def distance_correction(distance):
    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    while distance > 0.1: # TODO: Tune this threshold
        # Move the robot forward until the tag is head on
        cur_motor_command.trans_v = 0.1

    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    return

def angle_correction(angle):
    
    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0

    # Turn the robot until the z value ~0
    while angle > 0.15 or angle < -0.15: # TODO: Tune this threshold
        if angle > 0.15:
            cur_motor_command.angular_v = 0.1
        elif angle < -0.15:
            cur_motor_command.angular_v = -0.1

    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0
    
    return

# Go towards the april tag
@app.route('/', methods=['POST'])
def object_alignment():
    global angle
    global distance
    data = request.json

    if data.get('status') == 'DONE':
        print('DONE TRACKING TAG')
    else:
        # Update the angle and dustance of the tag
        angle = data.get('angle') #  TODO: make sure you can collect negative values
        distance = data.get('distance')

        # Correct Angle
        angle_correction(angle)

        # Correct Distance
        distance_correction(distance)
    
    # Return a success response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(host='0.0.0.0', port=5003, debug=True)



