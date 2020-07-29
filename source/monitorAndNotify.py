#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sys
from model.preference import Preference
from model.context import Context
from model.pushBullet import PushBullet
from model.database import Database
from model.fileHandle import File
from model.context import Context

def read_preference():
    # try:
    Preference.read_preference()
    # except:
    #     PushBullet.send_notification("From Raspberry Pi", "Fail to read files")
    #     sys.exit()

def reset():
    if (datetime.datetime.now().strftime("%H:%M") == "11:16"):
        if (Preference.comfortable_status == True):
            push_last_noti()
        else:
            save_status(True, Preference.create_new_table)

def push_last_noti():
    noti_body = "Average temperature of the day: " + get_avg_temp() + " Celsius"
    noti_body += "\nAverage humidity of the day: " + get_avg_humidity() + " %"
    noti_body += "\nSee you tomorrow! Good night"
    PushBullet.send_notification("From Raspberry Pi", noti_body)

def get_avg_temp():
    return str(round(Database.execute_equation(
        "AVG(temp)",
        " WHERE timestamp >= date('now','-1 day')"
    ), 2))

def get_avg_humidity():
    return str(round(Database.execute_equation(
        "AVG(humidity)",
        " WHERE timestamp >= date('now','-1 day')"
    ), 2))

def get_context_sense_hat():
    check_tb()
    Context.update_context()    
    Context.log_data_to_db()

def check_tb():
    if Preference.create_new_table == True:
        try:
            Database.create_tb(
                "(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)"
            )
            save_status(Preference.comfortable_status, False)
        except:
            PushBullet.send_notification("From Raspberry Pi", "Fail to create database table")
            sys.exit()

def check_context():
    Preference.check_context()
    if Context.temp_status != "good" or Context.humidity_status != "good":
        noti_body = Context.get_context_message()
        if Context.temp_status.find("too") == -1 and Context.humidity_status.find("too") == -1:
            if Preference.comfortable_status == True:
                PushBullet.send_notification("From Raspberry Pi", noti_body)
                save_status(False, Preference.create_new_table)
        else:
            PushBullet.send_notification("From Raspberry Pi", noti_body)
        

def save_status(comfortable_status, create_new_table):
    json_content = {
            "comfortable_status" : comfortable_status,
            "create_new_table" : create_new_table
    }
    File.write_json("status.json", json_content)
    read_preference()

def evaluate_context():
    read_preference()
    get_context_sense_hat()
    check_context()
    reset()
