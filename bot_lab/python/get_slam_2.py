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

odom_messages = []
slam_messages = []

odom_lock = threading.Lock()
slam_lock = threading.Lock()

def handle_message_odom(channel, data):
    msg = odometry_t.decode(data)
    with odom_lock:
        odom_messages.append((msg.utime, msg.x, msg.y, msg.theta))

def handle_message_slam(channel, data):
    msg = pose_xyt_t.decode(data)
    with slam_lock:
        slam_messages.append((msg.utime, msg.x, msg.y, msg.theta))

subscription_odom = lcm.subscribe("ODOMETRY", handle_message_odom)
subscription_slam = lcm.subscribe("SLAM_POSE", handle_message_slam)

try:
    while True:
        lcm.handle()
        time.sleep(0.5)
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
