import lcm
import time
import random
from lcmtypes import april_tag_data_t

APRILTAG_CHANNEL = "APRIL_TAG"

# Initialize LCM
lc = lcm.LCM('udpm://239.255.76.67:7667?ttl=2')

# Publish some sample AprilTag data
while True:
    # Create a sample AprilTag message
    tag_data = april_tag_data_t()
    tag_data.dist = 100
    tag_data.id = 1

    # Publish the message
    lc.publish(APRILTAG_CHANNEL, tag_data.encode())

    # Wait for a second
    time.sleep(1)
