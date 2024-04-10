# 467 Final Project - SimBot

## Teleop Gesture:

This repository contains code for teleoperation of Mbot using gestures. Follow the instructions below to set up and run the teleop_gesture program.

### Prerequisites

- Mbot
- Python 3
- Terminal

### Setup and Usage

1. Reflash the `*.uf2` file into Mbot.

2. Open three separate terminals.

In Terminal 1:
- Navigate to the `teleop_gesture/python/` directory:
  ```bash
  cd teleop_gesture/python/
    ```
- Write the following command, but do not run it yet:
  ```bash
  python3 teleop_gesture_v#.py
  ```
  (Replace # with the appropriate version number)

In Terminal 2:
- Navigate to the `teleop_gesture/shim_timesync_binaries/shim/` directory:
  ```bash
  cd teleop_gesture/shim_timesync_binaries/shim/
  ```
- Make the `shim` file executable:
  ```bash
  chmod +x ./shim
  ```
- Write the following command, but do not run it yet:
  ```bash
  ./shim
  ```

In Terminal 3:
- Navigate to the `teleop_gesture/shim_timesync_binaries/timesync/` directory:
  ```bash
  cd teleop_gesture/shim_timesync_binaries/
  ```
- Write the following command, but do not run it yet:
  ```bash
  ./timesync
  ```

3. Run the commands in the following order:
    - Terminal 1
    - Terminal 2
    - Terminal 3

Ensure that the terminals are running in the background to maintain the teleoperation functionality.

### Note

- Replace `teleop_gesture_v#.py` with the appropriate version of the Python script.
- Make sure to follow the order of commands as mentioned above for proper execution.
