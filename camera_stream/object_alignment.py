import numpy as np
from lcmtypes import mbot_motor_command_t
from lcmtypes import mbot_encoder_t

from flask import Flask, request, jsonify
app = Flask(__name__)

# Current angle of the robot to the april tag
angle = None

# Current distance of the robot to the april tag
distance = None

focal_length_x = 547.7837
focal_length_y = 547.8070
principal_point_x = 303.9048
principal_point_y = 243.7748

angle_threshold = 30

# Current motor command
cur_motor_command = mbot_motor_command_t()

def distance_correction(distance):
    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    while distance > 0.1: # TODO: Tune this threshold
        # Move the robot forward until the tag is head on
        print("MOVE FORWARD")
        cur_motor_command.trans_v = 0.1

    # Set linear velocity to 0.0 m/s
    cur_motor_command.trans_v = 0.0

    return

def angle_correction(angle):

    # Set angular velocity to 0 rad/s
    cur_motor_command.angular_v = 0.0

    # Turn the robot until the z value ~0
    while angle > (principal_point_x + angle_threshold) or angle < (principal_point_x - angle_threshold): # TODO: Tune this threshold
        if angle > principal_point_x:
            print("ANGLE RIGHT")
            cur_motor_command.angular_v = 0.1
        elif angle < principal_point_x:
            print("ANGLE LEFT")
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
    print("idle")
    if data.get('status') == 'DONE':
        print('DONE TRACKING TAG')
    else:
        # Update the angle and dustance of the tag
        angle = data.get('angle') #  TODO: make sure you can collect negative values
        distance = data.get('distance')
        print("received:" , angle, distance)

        # Correct Angle
        # angle_correction(angle)

        # Correct Distance
        distance_correction(distance)

    # Return a success response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(host='0.0.0.0', port=5003, debug=True)