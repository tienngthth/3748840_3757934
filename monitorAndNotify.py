#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sys
from model.preference import Preference
from model.context import Context
from model.senseHat import SenseHat
from model.pushBullet import PushBullet
from model.database import Database
from model.fileHandle import File
#from readAndDisplay import display_temp

def reset_status():
    if (datetime.datetime.now().strftime("%H:%M") == "00:00"):
        save_status("True", Preference.create_new_table)

def get_context_sense_hat():
    Context.set_context(SenseHat.get_data()[0:2])
    check_tb()
    log_data_to_db()

def check_tb():
    if Preference.create_new_table == "True":
        try:
            Database.create_tb(
                "SENSEHAT_data",
                "(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)"
            )
            save_status(Preference.comfortable_status, "False")
        except:
            PushBullet.send_notification("From Raspberry Pi", "Fail to create database table")
            sys.exit()

def log_data_to_db():
    parameters = (Context.time, Context.temp, Context.humidity)
    Database.insert_record("SENSEHAT_data", "((?), (?), (?))", parameters)

def check_context():
    status = Preference.check_comfortable(Context.temp)
    if status != "good" and Preference.comfortable_status == "True":
        body = "Temperature is too {}: {} celcius".format(status, Context.temp)
        PushBullet.send_notification("From Raspberry Pi", body)
        save_status("False", Preference.create_new_table)

def save_status(comfortable_status, create_new_table):
    json_content = {
            "comfortable_status" : comfortable_status,
            "create_new_table" : create_new_table
    }
    File.write_json("status.json", json_content)

def main():
    Preference.read_preference()
    reset_status()
    get_context_sense_hat()
    check_context()

main()