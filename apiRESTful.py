"""
Create a python file called apiRESTful.py which will contain RESTful APIs that
interact with the database. There should be 3 different methods involved as following:
1. GET: used to retrieve the newest temperature and humidity record with
timestamp in JSON format.
2. POST: used to upload a record to database with current timestamp.
3. PUT: used to update the newest record in database.
You also need to prepare a script to demonstrate that your API does work during the
demo session.
This script should be scheduled to automatically run when the Pi boots.

"""
import sys
from flask import Flask, request, jsonify
from model.database import Database
from model.context import Context
from model.pushBullet import PushBullet

app = Flask(__name__)

@app.route('/get/newest/context', methods=['GET'])
def get_context():
    try:
        return get_latest_context()
    except:
        PushBullet.send_notification("From Raspberry Pi", "Fail to update temperature")
        sys.exit()

def get_latest_context():
    record = Database.select_a_record("*",  "ORDER BY timestamp DESC LIMIT 1")
    json_content = {
        "timestamp" : record[0],
        "temp" : record[1],
        "humidity" : record[2]
    }
    return jsonify(json_content)

@app.route('/upload/context', methods=['POST'])
def upload_context():
    try:
        temp = request.json['temp']
        humidity = request.json['humidity']
        Context.update_context(temp, humidity)
        return "Successfully upload new context"
    except:
        return "Something went wrong with POST"

@app.route('/update/newest/context', methods=['POST'])
def update_context():
    update_temp()
    update_humidity()

def update_temp():
    temp = request.json['temp']
    try:
        if (temp != None):
            Database.update_last_record("temp", temp)
    except:
        PushBullet.send_notification("From Raspberry Pi", "Fail to update temperature")
        sys.exit()

def update_humidity():
    humidity = request.json['humidity']
    try:
        if (humidity != None):
            Database.update_last_record("humidity", humidity)
    except:
        PushBullet.send_notification("From Raspberry Pi", "Fail to update humidity")
        sys.exit()

if __name__ == "__main__":
    app.run(debug=True, port=8080)