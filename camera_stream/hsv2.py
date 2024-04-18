#attempt to read in from stream (failed)

from flask import Flask, request, Response
import cv2
import numpy as np

app = Flask(__name__)

# Function to detect red and green colors in a frame
def detect_colors(frame):
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and higher HSV values for the red color
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_red_wrap = np.array([170, 100, 100])
    upper_red_wrap = np.array([180, 255, 255])

    # Define the lower and higher HSV values for the green color
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

    # Create masks for red and green colors
    mask_red1 = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_red2 = cv2.inRange(hsv_frame, lower_red_wrap, upper_red_wrap)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Combine both masks
    mask = cv2.bitwise_or(mask_red, mask_green)

    # Find contours in the combined mask image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours and add a point to the center of each contour
    for contour in contours:
        # Draw contours on the frame
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        # Calculate the center of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Add a point to the center of the contour
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    return frame

@app.route('/image_receiver', methods=['POST'])
def receive_image():
    # Check if the request contains an image file
    if 'image' not in request.files:
        return 'No image file found', 400

    # Read the image file from the request
    image_file = request.files['image']
    
    # Convert the image file to a numpy array
    nparr = np.frombuffer(image_file.read(), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Detect colors, draw contours, and add points to the centers
    frame_with_contours = detect_colors(frame)

    # Encode the frame with contours and points back to JPEG format
    _, jpeg_img = cv2.imencode('.jpg', frame_with_contours)
    jpeg_bytes = jpeg_img.tobytes()

    # Return the processed image as a response
    return Response(jpeg_bytes, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
