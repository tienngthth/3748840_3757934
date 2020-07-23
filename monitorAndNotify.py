#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sys
from model.preference import Preference
from model.context import Context
from model.pushBullet import PushBullet
from model.database import Database
from model.fileHandle import File
from createReport import record_data

def read_preference():
    try:
        Preference.read_preference()
    except:
        PushBullet.send_notification("From Raspberry Pi", "Fail to read files")
        sys.exit()

def reset_status():
    if (datetime.datetime.now().strftime("%H:%M") == "00:00"):
        save_status("True", Preference.create_new_table)

def report_last_record():
    if (datetime.datetime.now().strftime("%H:%M") == "23:59"):
        record_data()
        if (Preference.comfortable_status == True):
            noti_body = "Average temperature of the day: " + get_avg_temp()
            noti_body += "\nAverage humidity of the day: " + get_avg_humidity()
            noti_body += "\n See you tomorrow! Good night"
            PushBullet.send_notification("From Raspberry Pi", noti_body)
            
def get_avg_temp():
    value = Database.execute_equation(
        "AVG(temp)",  
        "SENSEHAT_data", 
        "WHERE cast(timestamp as Date) = cast(getdate() as Date)"
    )
    return str(value)

def get_avg_humidity():
    value = Database.execute_equation(
        "AVG(humidity)",  
        "SENSEHAT_data", 
        "WHERE cast(timestamp as Date) = cast(getdate() as Date)"
    )
    return str(value)

def get_context_sense_hat():
    Context.update_context()
    check_tb()
    Context.log_data_to_db("SENSEHAT_data", "((?), (?), (?))")

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

def check_context():
    Preference.check_context()
    if Context.temp_status != "good" or Context.humidity_status != "good":
        noti_body = Context.get_context_message()
        if Context.temp_status.find("too") == -1 or Context.humidity_status.find("too") == -1:
            save_status("False", Preference.create_new_table)
        PushBullet.send_notification("From Raspberry Pi", noti_body)

def save_status(comfortable_status, create_new_table):
    json_content = {
            "comfortable_status" : comfortable_status,
            "create_new_table" : create_new_table
    }
    File.write_json("status.json", json_content)

def evaluate_context():
    read_preference()
    reset_status()
    get_context_sense_hat()
    check_context()
    report_last_record()
