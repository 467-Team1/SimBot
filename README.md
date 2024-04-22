# 467 Final Project - SimBot

## Prerequisites
- Mbot
- Python 3
- Terminal
- Wifi Router (Please be sure that both Local Machine and MBot are on the same network on the Wifi Router)
#### Hand Gesture Model Specifics
- mediapipe 0.8.1 (if using Mac, please download mediapipe 0.10.9)
- OpenCV 3.4.2 or Later
- Tensorflow 2.3.0 or Later
- tf-nightly 2.5.0.dev or later (Only when creating a TFLite for an LSTM model)
- scikit-learn 0.23.2 or Later (Only if you want to display the confusion matrix)
- matplotlib 3.3.2 or Later (Only if you want to display the confusion matrix)
#### April Tag
- Please Referance `AprilTag/README.md`

## Hand Gesture Model

### Setup and Usage

1. Open 1 terminal - **Locally**

In Terminal 1:
- Navigate to the `hand-gesture-recognition-mediapipe-main/` directory:
 ```bash
  cd hand-gesture-recognition-mediapipe-main/
  ```
- Run the following command:
  ```bash
  python3 app.py
  ```

## April Tag Recognition

### Setup and Usage

1. Open 3 terminals - **1 Locally** & **3 MBot**

In Terminal 1 (Mbot):
- Navigate to the `camera_stream/` directory:
  ```bash
  cd camera_stream
  ```
- Run the following command:
  ```bash
  python3 camerafinal.py
  ```

In Terminal 2 (Mbot):
- Navigate to the `camera_stream/` directory:
  ```bash
  cd camera_stream
  ```
- Run the following command:
  ```bash
  python3 object_alignment.py
  ```

In Terminal 3 (Locally):
- Navigate to the `AprilTag/scripts/` directory:
  ```bash
  cd AprilTag/scripts/
  ```
- Run the following command:
  ```bash
  python3 receive_stream.py
  ```

## Teleop Gesture

### Setup and Usage

1. Reflash the `*.uf2` file into Mbot.

2. Open three separate terminals - **MBot**

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
- Navigate to the `teleop_gesture/shim_timesync_binaries/` directory:
  ```bash
  cd teleop_gesture/shim_timesync_binaries/
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
- Navigate to the `teleop_gesture/shim_timesync_binaries/` directory:
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

## Note

- Replace `teleop_gesture_v#.py` with the appropriate version of the Python script.
- Make sure to follow the order of commands as mentioned above for proper execution.
- **Locally** means to open terminals on your local computer, *NOT* on the Mbot's Raspberry Pi

## Useful Commands
### To allow UI's to show up on VNC Viewer
```bash
ssh -X pi@[insert IP Address here]
```
once in the Raspberry Pi, run this command:
```bash
export DISPLAY=:0.0
```

