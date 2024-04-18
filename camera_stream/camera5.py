import io
import socket
import struct
import picamera
import time

# Set up the socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8000))
sock.listen(0)
conn, addr = sock.accept()
connection = conn.makefile('wb')

# Capture and send the video frames
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    time.sleep(2)  # Give the camera time to warm up
    stream = io.BytesIO()
    
    for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()
        stream.seek(0)
        connection.write(stream.read())
        stream.seek(0)
        stream.truncate()
