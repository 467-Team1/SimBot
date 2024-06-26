import lcm
import numpy as np
from lcmtypes import mbot_motor_command_t, timestamp_t
import time

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

DRIVE_LENGTH = 1
STOP_LENGTH = 0.2
ROTATE_LENGTH = 2

def current_utime(): return int(time.time() * 1e6)

# Rotate
rotate = mbot_motor_command_t()
rotate.utime = current_utime()
rotate.trans_v = 0.0
rotate.angular_v = np.pi #np.pi/2 $ np.pi

rotate_time = timestamp_t()
rotate_time.utime = rotate.utime
lc.publish("MBOT_TIMESYNC", rotate_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", rotate.encode())
time.sleep(ROTATE_LENGTH)

# Stop
stop = mbot_motor_command_t()
stop.utime = current_utime()
stop.trans_v = 0.0
stop.angular_v = 0.0

stop_time = timestamp_t()
stop_time.utime = stop.utime
lc.publish("MBOT_TIMESYNC", stop_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
time.sleep(STOP_LENGTH)