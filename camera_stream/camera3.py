import io
import time
import picamera
import requests

def capture_and_send_image():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        stream = io.BytesIO()

        for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
            # Reset stream position to the beginning
            stream.seek(0)
            
            # Send the image data as a POST request
            url = 'http://192.168.1.2:5000/image_receiver'
            files = {'image': stream}
            response = requests.post(url, files=files)
            
            # Reset stream for the next capture
            stream.seek(0)
            stream.truncate()

            # Sleep for a short time to control frame rate
            time.sleep(0.1)  # Adjust as needed

if __name__ == '__main__':
    capture_and_send_image()
