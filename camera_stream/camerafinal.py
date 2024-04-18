import io
import picamera
from flask import Flask, Response

app1 = Flask(__name__)

def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        stream = io.BytesIO()
        
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield stream.read()
            stream.seek(0)
            stream.truncate()

@app1.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    app1.run(host='192.168.1.4', port=5000, threaded=True)
