import sys
import time
import csv
import threading
sys.path.append("lcmtypes")
import lcm
from lcmtypes import particles_t
from lcmtypes import pose_xyt_t
from lcmtypes import odometry_t

lcm = lcm.LCM()

odom_accumulator = {'utime': 0, 'x': 0, 'y': 0, 'theta': 0, 'count': 0}
slam_accumulator = {'utime': 0, 'x': 0, 'y': 0, 'theta': 0, 'count': 0}

odom_messages = []
slam_messages = []

odom_lock = threading.Lock()
slam_lock = threading.Lock()

def handle_message_odom(channel, data):
    msg = odometry_t.decode(data)
    with odom_lock:
        odom_accumulator['utime'] += msg.utime
        odom_accumulator['x'] += msg.x
        odom_accumulator['y'] += msg.y
        odom_accumulator['theta'] += msg.theta
        odom_accumulator['count'] += 1

def handle_message_slam(channel, data):
    msg = pose_xyt_t.decode(data)
    with slam_lock:
        slam_accumulator['utime'] += msg.utime
        slam_accumulator['x'] += msg.x
        slam_accumulator['y'] += msg.y
        slam_accumulator['theta'] += msg.theta
        slam_accumulator['count'] += 1

subscription_odom = lcm.subscribe("ODOMETRY", handle_message_odom)
subscription_slam = lcm.subscribe("SLAM_POSE", handle_message_slam)

try:
    while True:
        lcm.handle()
        time.sleep(0.1)

        # Check if 0.1 seconds have passed
        if odom_accumulator['count'] > 0 and slam_accumulator['count'] > 0:
            # Calculate averages
            with odom_lock:
                odom_avg = [odom_accumulator[key] / odom_accumulator['count'] for key in ['utime', 'x', 'y', 'theta']]
                odom_messages.append(odom_avg)
                # Reset accumulator
                odom_accumulator = {'utime': 0, 'x': 0, 'y': 0, 'theta': 0, 'count': 0}

            with slam_lock:
                slam_avg = [slam_accumulator[key] / slam_accumulator['count'] for key in ['utime', 'x', 'y', 'theta']]
                slam_messages.append(slam_avg)
                # Reset accumulator
                slam_accumulator = {'utime': 0, 'x': 0, 'y': 0, 'theta': 0, 'count': 0}

except KeyboardInterrupt:
    pass

# Write data to CSV files
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['utime', 'x', 'y', 'theta'])
        csvwriter.writerows(data)

write_to_csv('odom_data.csv', odom_messages)
write_to_csv('slam_data.csv', slam_messages)