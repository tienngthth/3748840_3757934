#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
import requests
import datetime
import sys
import pathlib
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
token = "o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj"
dbname = "sensehat.db"

class Preference:
    def __init__(self, cold_max, comfortable_min, comfortable_max, hot_min, comfortable_status):
        self.cold_max = cold_max
        self.comfortable_min = comfortable_min
        self.comfortable_max = comfortable_max
        self.hot_min = hot_min
        self.comfortable_status = comfortable_status

    def check_comfortable(self, temp):
        if temp > self.comfortable_max:
            return "hot"
        elif temp < self.comfortable_min:
            return "cold"
        else:
            return "good"

    def set_comfortable_status(self, status):
        self.comfortable_status = status

class Context:
    def __init__(self, temp, humidity):
        self.time = datetime.datetime.now()
        self.temp = round(temp, 2)
        self.humidity = round(humidity, 2)

def read_files():

    try:
        config_file = open(pathlib.Path(__file__).parent / "config.json")
        config_json = json.load(config_file)
        status_file = open(pathlib.Path(__file__).parent / "status.json")
        status_json = json.load(status_file)
        get_preference(config_json, status_json)
        check_tb(status_json)
    except:
        send_notification_via_pushbullet("From Raspberry Pi", "Fail to read files")
        sys.exit()

def get_preference(config_json, status_json):
    global preference
    preference = Preference (
        float(config_json["cold_max"]),
        float(config_json["comfortable_min"]),
        float(config_json["comfortable_max"]),
        float(config_json["hot_min"]),
        status_json["comfortable_status"]
    )

def check_tb(status_json):
    try:
        if status_json["new_tb"] == "True":
            con = sqlite3.connect("sensehat.db")
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
            cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
    except:
        send_notification_via_pushbullet("From Raspberry Pi", "Fail to create database table")
        sys.exit()

def get_context_sense_hat():
    global context
    context = Context(sense.get_temperature(), sense.get_humidity())
    log_data_to_db(context)

def log_data_to_db(context):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute(
        "INSERT INTO SENSEHAT_data values((?), (?), (?))",
        (context.time, context.temp, context.humidity)
    )
    conn.commit()
    conn.close()
    display_db()

def display_db():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()

def check_context():
    status = preference.check_comfortable(context.temp)
    if status != "good" and preference.comfortable_status == "True":
        body = "Temperature is too {}: {} celcius".format(status, context.temp)
        send_notification_via_pushbullet("From Raspberry Pi", body)
        save_status("False", "False")

def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body}
    resp = requests.post(
        'https://api.pushbullet.com/v2/pushes',
        data=json.dumps(data_send),
        headers={'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'}
    )
    if resp.status_code != 200:
        raise Exception('something wrong')
    else:
        print('complete sending')

def save_status(comfortable_status, new_tb):
    status_file = open(pathlib.Path(__file__).parent / "status.json", "w")
    status_file.write(json.dumps({
            "comfortable_status" : comfortable_status,
            "new_tb" : new_tb
        }))
    status_file.close()

def reset_status():
    if (datetime.datetime.now().strftime("%H:%M") == "17:18"):
        save_status("True", "False")

def main():
    sense.show_message("hi")
    reset_status()
    read_files()
    get_context_sense_hat()
    check_context()

main()