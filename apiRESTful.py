"""
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
        return "Fail to get context"

def get_latest_context():
    record = Database.select_a_record("*",  " ORDER BY timestamp DESC LIMIT 1")
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
        if check_float(str(temp)) and check_float(str(humidity)):
            Context.update_context(temp, humidity)
            return "Successfully upload new context"
        else:
            return "Wrong temperture or humidity format"
    except:
        return "Fail to create new context"

@app.route('/update/newest/context', methods=['PUT'])
def update_context():
    return update_temp() + "\n" + update_humidity()

def update_temp():
    try:
        temp = request.json['temp']
        if check_float(str(temp)):
            Database.update_last_record("temp", (temp,))
            return "Successfully update temperature"
        else:
            return "Wrong temperture format"
    except:
        return "Fail to update temperature"

def update_humidity():
    try:
        humidity = request.json['humidity']
        if check_float(str(humidity)):
            Database.update_last_record("humidity", (humidity,))
            return "Successfully update humidity"
        else:
            return "Wrong humidity format"
    except:
        return "Fail to update humidity"

def check_float(float_string):
    if float_string.find(".") != -1:
        return float_string.replace('.', '', 1).isdigit()
    else:
        return float_string.isdigit()

if __name__ == "__main__":
    app.run(debug=True, port=8080)