from flask import Flask, request
import os
import cv2
from apriltag import Detector

app = Flask(__name__)

@app.route('/image_receiver', methods=['POST'])
def receive_image():
    # Check if the request contains an image file
    if 'image' not in request.files:
        return 'No image file found', 400

    image_file = request.files['image']
    
    # Read the image file into a numpy array
    np_img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Run AprilTag detection on the received image
    detections = detector.detect(np_img)
    
    # Process the detections (e.g., draw bounding boxes)
    for detection in detections:
        # Extract tag ID and corners
        tag_id = detection['id']
        corners = detection['corners']
        
        # Draw a bounding box around the detected tag
        cv2.polylines(np_img, [corners], True, (0, 255, 0), thickness=2)
        
        # Put tag ID as text on the image
        cv2.putText(np_img, f"Tag ID: {tag_id}", (corners[0][0], corners[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Encode the processed image back to JPEG format
    _, jpeg_img = cv2.imencode('.jpg', np_img)
    
    # Convert the encoded image to bytes
    jpeg_bytes = jpeg_img.tobytes()

    with open('detected_apriltags.jpg', 'wb') as f:
        f.write(jpeg_bytes)

    # Save the image to a file
    # image_path = '/path/to/save/image.jpg'
    # image_file.save(image_path)
    
    return 'Image received and saved successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
