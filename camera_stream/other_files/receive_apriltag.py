from flask import Flask, request, Response, render_template
import cv2
import numpy as np
import apriltag

app = Flask(__name__)

# Your AprilTag detection function
def detect_apriltags(frame):
    detector = apriltag.Detector()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = detector.detect(gray)
    return result

# Route to handle video reception
@app.route('/video_receiver', methods=['POST'])
def video_receiver():
    # Get the video file from the POST request
    video_file = request.files['video']

    # Read the video file into a numpy array
    nparr = np.frombuffer(video_file.read(), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Perform AprilTag detection on the received frame
    detections = detect_apriltags(frame)

    # Draw AprilTag detections on the frame
    for detection in detections:
        # Get the corners of the detected AprilTag
        corners = np.array(detection.corners, dtype=np.int32)
        corners = corners.reshape((-1, 1, 2))
        
        # Draw the AprilTag outline on the frame
        cv2.polylines(frame, [corners], True, (0, 255, 0), 2)
        
        # Put the AprilTag ID on the frame
        cv2.putText(frame, str(detection.tag_id), (corners[0][0][0], corners[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Convert the frame to JPEG format
    ret, jpeg = cv2.imencode('.jpg', frame)
    jpeg_bytes = jpeg.tobytes()

    return Response(jpeg_bytes, mimetype='image/jpeg')

# Route to serve HTML template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
