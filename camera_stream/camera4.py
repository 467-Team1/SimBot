import io
import time
import picamera
import requests

def capture_and_send_image():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        stream = io.BytesIO()

        while True:
            # Capture an 
            print("1\n")
            camera.capture(stream, 'jpeg', use_video_port=True)
            stream.seek(0)
            
            # Send the image data as a POST request
            url = 'http://192.168.1.2:5000/image_receiver'
            files = {'image': stream.read()}
            response = requests.post(url, files=files)
            
            # Reset stream for the next capture
            stream.seek(0)
            stream.truncate()
            
            # Wait for 1 second
            time.sleep(0.1)

if __name__ == '__main__':
    capture_and_send_image()
