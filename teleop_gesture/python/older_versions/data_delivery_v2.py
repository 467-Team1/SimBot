from flask import Flask, request, jsonify
import lcm
import time
import random
from lcmtypes import april_tag_data_t

APRILTAG_CHANNEL = "APRIL_TAG"


# Initialize LCM
lc = lcm.LCM('udpm://239.255.76.67:7667?ttl=2')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def data_deliver():
    data = request.json

    if data.get('status') == 'DONE' or data.get('status') == "Out of Sight":
        print('DONE TRACKING TAG')
        with open('data.txt','w'):
            pass
    elif (data.get('status') == 'DONE DOUBLE'):
        print('DONE DOUBLE')
        print("Distance:", data.get('distance'))
        with open('data.txt','w'):
            pass
        
        tag_data = april_tag_data_t()
        tag_data.dist = data.get('distance')
        tag_data.id = data.get('id')
        
        lc.publish(APRILTAG_CHANNEL, tag_data.encode())

        time.sleep(1)

    else:
        # Assuming the data includes 'corners' and 'distance' as sent by your application
        angle = data.get('angle')
        distance = data.get('distance')
        print("Angles:", angle)
        print("Distance:", distance)

        if angle is None or distance is None:
            print("Nonetype received...")
            return jsonify({'status': 'success'}), 200

        if (data.get('log') == 'log'):
            #double click
            with open('data.txt','w') as file:
                file.write(str(angle) + " " + str(distance) + " " + str(id) + " " + "log")
        else:
            with open('data.txt','w') as file:
                file.write(str(angle) + " " + str(distance))
    
    # Return a success response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(host='0.0.0.0', port=5003, debug=True)
