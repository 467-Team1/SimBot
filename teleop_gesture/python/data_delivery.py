from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['POST'])
def data_deliver():
    data = request.json

    if data.get('status') == 'DONE' or data.get('status') == "Out of Sight":
        print('DONE TRACKING TAG')
        with open('data.txt','w'):
            pass
    else:
        # Assuming the data includes 'corners' and 'distance' as sent by your application
        angle = data.get('angle')
        distance = data.get('distance')
        print("Angles:", angle)
        print("Distance:", distance)

        if angle is None or distance is None:
            print("Nonetype received...")
            return jsonify({'status': 'success'}), 200

        with open('data.txt','w') as file:
            file.write(str(angle) + " " + str(distance))
    
    # Return a success response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(host='0.0.0.0', port=5003, debug=True)
