# 467 Final Project - SimBot
## Authors
- [Laasya Chukka](https://github.com/lchukka450) - [lchukka@umich.edu](mailto:lchukka@umich.edu)
- [Ansh Mehta](https://github.com/anshm10) - [anshm@umich.edu](mailto:anshm@umich.edu)
- [Christian Vega](https://github.com/cpgvega) - [email@example.com](mailto:cpvega@umich.edu)
- [Wendi Zhang](https://github.com/zwendi123) - [zwendi@umich.edu](mailto:zwendi@umich.edu)

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
- AprilTag repo is not specifically in the repository, you will need to clone it locally to your machine (This is due to dependancies in CMake that are specific to your machine)
- Please Refer to `april_tag/README.md` for details
- Add `templates/` directory & `receive_stream.py` from the `support_files` directory to the `AprilTag/scripts/` directory
  ```bash
  cp -r support_files/ AprilTag/scripts/
  ```

## Demo of Final Project
<iframe width="560" height="315" src="https://youtu.be/FMWMjoAIFdI" frameborder="0" allowfullscreen></iframe>

## April Tag Recognition

### Setup and Usage

1. Open 3 terminals - **1 Locally** & **2 MBot**

In Terminal 1 (Mbot):
- Navigate to the `camera_stream/` directory:
  ```bash
  cd camera_stream
  ```
- Run the following command:
  ```bash
  python3 camera_final.py
  ```

In Terminal 2 (Locally):
- Navigate to the `april_tag/scripts/` directory:
  ```bash
  cd april_tag/scripts/
  ```
- Run the following command:
  ```bash
  python3 receive_stream.py
  ```

In Terminal 3 (Mbot):
- Navigate to the `teleop_gesture/python/` directory:
  ```bash
  cd teleop_gesture/python/
  ```
- Run the following command:
  ```bash
  python3 data_delivery.py
  ```

## Teleop Gesture

### Setup and Usage

1. Reflash the `*.uf2` file into Mbot.

2. Open three separate terminals - **3 MBot**

In Terminal 1 (Mbot):
- Navigate to the `teleop_gesture/shim_timesync_binaries/` directory:
  ```bash
  cd teleop_gesture/shim_timesync_binaries/
  ```
- Give the `shim` file permission to execute:
  ```bash
  chmod +x shim
  ```
- Run the following command:
  ```bash
  ./shim
  ```

In Terminal 2 (Mbot):
- Navigate to the `teleop_gesture/shim_timesync_binaries/` directory:
  ```bash
  cd teleop_gesture/shim_timesync_binaries/
  ```
- Run the following command:
  ```bash
  ./timesync
  ```

In Terminal 3 (Mbot):
- Navigate to the `teleop_gesture/python/` directory:
  ```bash
  cd teleop_gesture/python/
  ```
- Run the following command:
  ```bash
  python3 teleop_gesture_v#.py
  ```
  (Replace # with the appropriate version number)

3. Run the commands in the following order:
    - Terminal 1
    - Terminal 2
    - Terminal 3

Ensure that the terminals are running in the background to maintain the teleoperation functionality.

## Hand Gesture Model

### Setup and Usage

1. Open 1 terminal - **1 Locally**

In Terminal 1 (Locally):
- Navigate to the `hand_gesture_recognition_mediapipe_main/` directory:
 ```bash
  cd hand_gesture_recognition_mediapipe_main/
  ```
- Run the following command:
  ```bash
  python3 app.py
  ```

  ## SLAM
  1. Ensure that the LIDAR is plugged in and turned on

  2. Open three separate terminals - **3 MBot**

  In Terminal 1 (Mbot):
  - Navigate to the `bot_lab/bin/` directory:
  ```bash
  cd bot_lab/bin/
  ```

  - Run the following command:
  ```bash
  ./rplidar_driver
  ```

  In Terminal 2 (Mbot):
  - Navigate to the `bot_lab/bin/` directory:
  ```bash
  cd bot_lab/bin/
  ```

  - Run the following command:
  ```bash
  ./slam
  ```

  - Navigate to the `bot_lab/` directory:
  ```bash
  cd bot_lab/
  ```

  - Run the following command:
  ```bash
  source setenv.sh
  ```

  - Navigate to the `bin/` directory:
  ```bash
  cd bin/
  ```

  - Run the following command: [Link to "To allow UI's to show up on VNC Viewer"](#vnc-ui)
  ```bash
  ./botgui
  ```

## Note
- Replace `teleop_gesture_v#.py` with the appropriate version of the Python script.
- Make sure to follow the order of commands as mentioned above for proper execution.
- **Locally** means to open terminals on your local computer, *NOT* on the Mbot's Raspberry Pi
- The following require that you update the IP address from the Mbot ```ifconfig``` use the wlan0 IP address:
  - camerafinal.py; line 26
  - app.py; line 47
  - teleop_gesture_v3.py; line 42
  - receive_stream.py; line 31

## Useful Commands
### To allow UI's to show up on VNC Viewer {#vnc-ui}
```bash
ssh -X pi@[insert Mbot IP Address here]
```
once in the Raspberry Pi, run this command:
```bash
export DISPLAY=:0.0
```

### To link receive_stream.py; allowing changes in your personal cloned AprilTag's receive_stream.py to support/receive_stream.py
```bash
ln AprilTag/scripts/receive_stream.py support_files/receive_stream.py
```
You might need to move support_files/receive_stream.py out of the it's directory momentarily for this to work (after you added a copy into AprilTag/scripts)

## References
- [hand-gesture-recognition-using-mediapipe](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe.git)
- [AprilTag](https://github.com/Tinker-Twins/AprilTag.git)

