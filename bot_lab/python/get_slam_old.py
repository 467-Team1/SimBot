import sys
import time
sys.path.append("lcmtypes")
import lcm
from lcmtypes import particles_t
from lcmtypes import pose_xyt_t
from lcmtypes import odometry_t
lcm = lcm.LCM()
import numpy as np
import threading
import time 




def calculate_points(list):
    sum_x = sum(point.x for point in list)
    sum_y = sum(point.y for point in list)
    return ((sum_x, sum_y))

start_time = time.perf_counter()
def handle_message_odom(channel, data):
    
    msg = odometry_t.decode(data)
    # print("ODOM", msg.utime, msg.x, msg.y)
    mini_odom.append(msg)
    end_time = time.perf_counter()
    if (end_time - start_time > 0.1):
        start_time = time.perf_counter()
        odom_messages.append(calculate_points(mini_odom))
        mini_odom = []
    
        
    # msg = particles_t.decode(data).particles
    # print(msg[0].pose.x, msg[0].pose.y, msg[0].pose.theta)


def handle_message_slam(channel, data):
    msg = pose_xyt_t.decode(data)
    # print("SLAM", msg.utime, msg.x, msg.y)
    mini_slam.append(msg)
    end_time = time.perf_counter()
    # msg = particles_t.decode(data).particles
    # print(msg[0].pose.x, msg[0].pose.y, msg[0].pose.theta)
    if (end_time - start_time > 0.1):
        start_time = time.perf_counter()
        slam_messages.append(calculate_points(mini_slam))
        mini_slam = []

# lc = lcm.LCM()
subscription_odom = lcm.subscribe("ODOMETRY", handle_message_odom)
subscription = lcm.subscribe("SLAM_POSE", handle_message_slam)

try:
    global odom_messages 
    global slam_messages 

    global mini_odom 
    global mini_slam 
    odom_messages = []
    slam_messages = [] 

    mini_odom = []
    mini_slam = []
    
    while True:
        
        lcm.handle()
except KeyboardInterrupt:
    f = open("odom.csv", "a")
    f.write(odom_messages)
    f.close()

    f = open("slam.csv", "a")
    f.write(slam_messages)
    f.close()
    
    pass