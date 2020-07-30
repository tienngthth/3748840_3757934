#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from model.database import Database
from model.context import Context
from model.util import Util

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
        if Util.check_float(str(temp)) and Util.check_float(str(humidity)):
            Context().update_context(temp, humidity, None, True)
            return "Successfully upload new context"
        else:
            return "Wrong temperture or humidity format, invalid number"
    except:
        return "Fail to create new context"

@app.route('/update/newest/context', methods=['PUT'])
def update_context():
    return update_temp() + "\n" + update_humidity()

def update_temp():
    try:
        temp = request.json['temp']
        if Util.check_float(str(temp)):
            Database.update_last_record("temp", (temp,))
            return "Successfully update temperature"
        else:
            return "Wrong temperture format, invalid number"
    except:
        return "Fail to update temperature"

def update_humidity():
    try:
        humidity = request.json['humidity']
        if Util.check_float(str(humidity)):
            Database.update_last_record("humidity", (humidity,))
            return "Successfully update humidity"
        else:
            return "Wrong humidity format, invalid number"
    except:
        return "Fail to update humidity"

if __name__ == "__main__":
    app.run(debug=True, port=8080)