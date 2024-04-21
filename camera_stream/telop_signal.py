from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.json

    if data.get('status') == 'DONE':
        print('DONE TRACKING TAG')
    else:
        # Assuming the data includes 'corners' and 'distance' as sent by your application
        angle = data.get('angle')
        distance = data.get('distance')
        headon = data.get('headon')
        print("Angles:", angle)
        print("Distance:", distance)
        print("Head ON:", headon)
    
    # Return a success response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(host='0.0.0.0', port=5003, debug=True)
