from flask import Flask, Response, render_template, request, jsonify
import requests
from apriltag import Detector
import cv2
import numpy as np
from threading import Lock
import socket

app2 = Flask(__name__)

detector = Detector()

tags_lock = Lock()

detected_tags = []


focal_length_x = 547.7837  
focal_length_y = 547.8070
principal_point_x = 303.9048  
principal_point_y = 243.7748

tag_height_meters = 0.05 # TODO: make sure to change for specific april tag 

@app2.route('/april_tag_click', methods=['POST'])
def april_tag_click():
    with tags_lock:
        data = request.get_json()

        # Check if the data is valid
        if not data:
            return jsonify({'error': 'Invalid data'}), 400

        x, y = data.get('x'), data.get('y')

        # Check if the click is inside any of the detected tags
        for tag in detected_tags:
            if x >= tag['xMin'] and x <= tag['xMax'] and y >= tag['yMin'] and y <= tag['yMax']:
                (cX, cY) = (int((tag['xMin'] + tag['xMax']) / 2), int((tag['yMin'] + tag['yMax']) / 2))

                x_physical = (cX - principal_point_x) / focal_length_x
                y_physical = (cY - principal_point_y) / focal_length_y
                z_physical = 1 

                print("[INFO] AprilTag center physical coordinates (x, y, z): ({:.2f}, {:.2f}, {:.2f})".format(
                    x_physical, y_physical, z_physical))

                # Distance from camera to tag - NEEDED for cenering the robot
                distance = -1 * (tag_height_meters * focal_length_y) / (tag['yMin'] - tag['yMax'])

                # Print the distance to the HTML page
                message_dist = ("[INFO] Distance to AprilTag: {:.2f} meters".format(distance))
                return jsonify({'message': message_dist})
        
        return jsonify({'message': 'Clicked outside of all tags'})

@app2.route('/')
def index():
    return render_template('index.html')

@app2.route('/video')
def video():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

def get_frames():
    url = 'http://192.168.1.2:5000/video_feed'  
    response = requests.get(url, stream=True)

    frame_buffer = b''

    for chunk in response.iter_content(chunk_size=1024):
        frame_buffer += chunk
        frame_end = frame_buffer.find(b'\xff\xd9')  
        while frame_end != -1:
            frame_start = frame_buffer.find(b'\xff\xd8')  
            if frame_start != -1:
                frame = frame_buffer[frame_start:frame_end + 2]

                processed_frame = process_frame(frame)

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + processed_frame + b'\r\n')

                frame_buffer = frame_buffer[frame_end + 2:]

            frame_end = frame_buffer.find(b'\xff\xd9')

def process_frame(frame):
    global detected_tags  

    nparr = np.frombuffer(frame, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    results = detector.detect(gray)

    with tags_lock:
        detected_tags.clear()
        for r in results:
            corners = np.array(r.corners, dtype=np.int32)
            cv2.polylines(image, [corners], True, (0, 255, 0), 2)
            tag = {
                'xMin': int(corners[:, 0].min()),
                'yMin': int(corners[:, 1].min()),
                'xMax': int(corners[:, 0].max()),
                'yMax': int(corners[:, 1].max())
            }
            detected_tags.append(tag)

    #-HSV stuff-----------------------------------------
    nparr = np.frombuffer(frame, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert frame to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define HSV color range for detection
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

    # Create mask to isolate green color
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process contours
    for contour in contours:
        # Filter contours based on criteria (e.g., area)
        area = cv2.contourArea(contour)
        if area > 100:
            # Get bounding box of contour
            x, y, w, h = cv2.boundingRect(contour)
            # Draw bounding box on original frame
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calculate tag center
            cX = x + w // 2
            cY = y + h // 2
            # Append detected tag to the list
            detected_tags.append({
                'xMin': x,
                'yMin': y,
                'xMax': x + w,
                'yMax': y + h,
                'centerX': cX,
                'centerY': cY
            })
    #-end of hsv stuff------------------------

    ret, buffer = cv2.imencode('.jpg', image)
    return buffer.tobytes()

if __name__ == '__main__':
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    app2.run(host=IP, port=5001, threaded=True)