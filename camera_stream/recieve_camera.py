from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/image_receiver', methods=['POST'])
def receive_image():
    # Check if the request contains an image file
    if 'image' not in request.files:
        return 'No image file found', 400

    image_file = request.files['image']
    
    # Save the image to a file
    image_path = '/path/to/save/image.jpg'
    image_file.save(image_path)
    
    return 'Image received and saved successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
