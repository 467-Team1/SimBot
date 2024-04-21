'''
This program should run after an april tag/colored block has be clicked on.

Step 1: The robot will receive the corners of the april tag on the frame 
and the distance from the april tag

Step 2: Use the pose received from the april tag to calculate the angle 
between the robot  and the april tag

Step 3: The robot will rotate until the z angle is 0.

Step 4: Once the april tag is approximately at the center. the robot will move forward 
until the distance is lower than a threshold value to avoid colliding with the object

Step 5: The robot will run the claw code

Step 6: Switch back to teleop gesture control
'''