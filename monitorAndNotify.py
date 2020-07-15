#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
import requests
import datetime
import sys
import pathlib
from model.preference import Preference
from model.context import Context
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
token = "o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj"
dbname = "sensehat.db"

def read_files():
    try:
        config_file = open(pathlib.Path(__file__).parent / "config.json")
        config_json = json.load(config_file)
        status_file = open(pathlib.Path(__file__).parent / "status.json")
        status_json = json.load(status_file)
        get_preference(config_json, status_json)
    except:
        send_notification_via_pushbullet("From Raspberry Pi", "Fail to read files")
        sys.exit()

def get_preference(config_json, status_json):
    Preference.set_preference (
        float(config_json["cold_max"]),
        float(config_json["comfortable_min"]),
        float(config_json["comfortable_max"]),
        float(config_json["hot_min"]),
        status_json["comfortable_status"],
        status_json["create_new_table"]
    )

def get_context_sense_hat():
    Context.set_context(sense.get_temperature(), sense.get_humidity())
    check_tb()
    log_data_to_db()

def check_tb():
    try:
        if preference.new_tb == "True":
            con = sqlite3.connect("sensehat.db")
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
            cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
    except:
        send_notification_via_pushbullet("From Raspberry Pi", "Fail to create database table")
        sys.exit()

def log_data_to_db():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute(
        "INSERT INTO SENSEHAT_data values((?), (?), (?))",
        (Context.time, Context.temp, Context.humidity)
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
    status = Preference.check_comfortable(Context.temp)
    if status != "good" and Preference.comfortable_status == "True":
        body = "Temperature is too {}: {} celcius".format(status, Context.temp)
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