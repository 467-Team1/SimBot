import os
import sys

import lcm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from lcmtypes import mbot_encoder_t, mbot_motor_command_t, timestamp_t, odometry_t, pose_xyt_t


def is_between(a, b, c):
    return a <= c <= b or b <= c <= a


sys.path.append("lcmtypes")

WHEEL_BASE = 0.15
WHEEL_DIAMETER = 0.084
GEAR_RATIO = 78
ENCODER_RES = 20
enc2meters = WHEEL_DIAMETER * np.pi / (GEAR_RATIO * ENCODER_RES)

if len(sys.argv) < 2:
    sys.stderr.write("usage: plot_step.py <logfile>")
    sys.exit(1)

file = sys.argv[1]
log = lcm.EventLog(file, "r")

encoder_data = np.empty((0, 5), dtype=int)
encoder_init = 0

command_data = np.empty((0, 3), dtype=float)
command_init = 0

timesync_data = np.empty((0, 1), dtype=int)

odom_data = np.empty((0, 2), dtype=float)
slam_data = np.empty((0, 2), dtype=float)
true_pose_data = np.empty((0, 2), dtype=float)

for event in log:
    if event.channel == "MBOT_ENCODERS":
        encoder_msg = mbot_encoder_t.decode(event.data)
        if encoder_init == 0:
            enc_start_utime = encoder_msg.utime
            print("enc_start_utime: {}".format(enc_start_utime))
            encoder_init = 1
        encoder_data = np.append(encoder_data, np.array([[
            (encoder_msg.utime - enc_start_utime)/1.0E6,
            encoder_msg.leftticks,
            encoder_msg.rightticks,
            encoder_msg.left_delta,
            encoder_msg.right_delta
        ]]), axis=0)

    if event.channel == "MBOT_MOTOR_COMMAND":
        command_msg = mbot_motor_command_t.decode(event.data)
        if command_init == 0:
            cmd_start_utime = command_msg.utime
            print("cmd_start_utime: {}".format(cmd_start_utime))
            command_init = 1
        command_data = np.append(command_data, np.array([[
            (command_msg.utime - cmd_start_utime)/1.0E6,
            command_msg.trans_v,
            command_msg.angular_v
        ]]), axis=0)

    if event.channel == "MBOT_TIMESYNC":
        timesync_msg = timestamp_t.decode(event.data)
        timesync_data = np.append(timesync_data, np.array([[
            (timesync_msg.utime)/1.0E6,
        ]]), axis=0)
        
    if event.channel == "ODOMETRY":
        odom_msg = odometry_t.decode(event.data)
        odom_data = np.append(odom_data, np.array([[
            odom_msg.x, odom_msg.y
        ]]), axis=0)

    if event.channel == "SLAM_POSE":
        slam_msg = pose_xyt_t.decode(event.data)
        slam_data = np.append(slam_data, np.array([[
            slam_msg.x, slam_msg.y
        ]]), axis=0)

    if event.channel == "TRUE_POSE":
        true_pose_msg = pose_xyt_t.decode(event.data)
        true_pose_data = np.append(true_pose_data, np.array([[
            true_pose_msg.x, true_pose_msg.y
        ]]), axis=0)


# Encoder data
enc_time = encoder_data[:, 0]
enc_time_diff = np.diff(enc_time)
leftticks = encoder_data[:, 1]
rightticks = encoder_data[:, 2]
left_delta = encoder_data[:, 3]
right_delta = encoder_data[:, 4]

# Compute the wheel velocities from encoders
left_measured_vel = np.diff(leftticks) * enc2meters / enc_time_diff
right_measured_vel = np.diff(rightticks) * enc2meters / enc_time_diff


# print(timesync_data[0, 0], timesync_data[1, 0])

# Wheel command data
cmd_time = command_data[:, 0]
# print(cmd_time[0] , cmd_time[1])
trans_v = command_data[:, 1]
angular_v = command_data[:, 2]
left_setpoint_vel = trans_v - WHEEL_BASE * angular_v / 2
right_setpoint_vel = trans_v + WHEEL_BASE * angular_v / 2
left_setpoint_vel = np.insert(left_setpoint_vel, 0, 0)
right_setpoint_vel = np.insert(right_setpoint_vel, 0, 0)

# Repeat each item in the setpoint lists twice in a numpy array
left_setpoint_vel = np.repeat(left_setpoint_vel, 2)
right_setpoint_vel = np.repeat(right_setpoint_vel, 2)

# Move the command points to the frst time where the encoders change
# possible issue as this is not a great solution
first_enc_change_left = np.where(left_delta != 0)[0][0]
first_enc_change_right = np.where(right_delta != 0)[0][0]

i = 1
while first_enc_change_left != first_enc_change_right:
    first_enc_change_left = np.where(left_delta != 0)[0][i]
    first_enc_change_right = np.where(right_delta != 0)[0][i]
    i += 1

# Start forming the command lines
left_cmd_times = cmd_time + enc_time[first_enc_change_left]
right_cmd_times = cmd_time + enc_time[first_enc_change_right]
left_cmd_times = np.repeat(left_cmd_times, 2)
right_cmd_times = np.repeat(right_cmd_times, 2)

# Add a value to the beginning of the command lines to make them start at the same time
left_cmd_times_ = np.ones((left_cmd_times.shape[0] + 2)) * enc_time[1]
right_cmd_times_ = np.ones((right_cmd_times.shape[0] + 2)) * enc_time[1]
left_cmd_times_[1:-1] = left_cmd_times
right_cmd_times_[1:-1] = right_cmd_times
left_cmd_times_[-1] = enc_time[-1]
right_cmd_times_[-1] = enc_time[-1]


# print(true_pose_data.shape)
# print(slam_data.shape)
true_pose_data = np.array_split(true_pose_data, len(slam_data))
new_true_data = np.zeros((len(slam_data), 2), dtype=float)
# print(true_pose_data)

enc_time = np.array_split(enc_time, len(slam_data))
new_time_data = np.zeros((len(slam_data)), dtype=float)
for i in range(len(slam_data)):
    tmp = true_pose_data[i]
    for j in range(len(tmp)):
        new_true_data[i] += tmp[j]
    new_true_data[i] /= len(tmp)

for i in range(len(slam_data)):
    tmp = enc_time[i]
    for j in range(len(tmp)):
        new_time_data[i] += tmp[j]
    new_time_data[i] /= len(tmp)
RMS_error = np.sqrt(np.sum((slam_data-new_true_data)**2, axis=1) / len(slam_data))
# squared_diff = np.square(slam_data - new_true_data)
# print(squared_diff[:2])

# mean_squared_diff = np.mean(squared_diff, axis=0)

# RMS_error = np.sqrt(mean_squared_diff)

# print(RMS_error)

fig, ax = plt.subplots(1, 1, sharey=True, figsize=(10, 10))
ax.plot(new_time_data, RMS_error, 'b')
ax.set_xlabel("Time (s)")
ax.set_ylabel("RMS error (m)")

ax.set_ylim(0, 1)

# plt.savefig(f"{file}.png")
plt.savefig("RMS_error.png")

plt.show()