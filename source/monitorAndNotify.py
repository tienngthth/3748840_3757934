#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sys
from model.preference import Preference
from model.context import Context
from model.pushBullet import PushBullet
from model.database import Database
from model.fileHandle import File
from model.util import Util

def start_program():
    global preference, context
    context = Context()
    preference = Util.read_preference()

def get_context_sense_hat():
    check_tb()
    context.update_real_time_context()    

def check_tb():
    if preference.create_new_table == True:
        try:
            Database.create_tb(
                "(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)"
            )
            preference.create_new_table = False
        except:
            print("Fail to create new database table")
            sys.exit()

def check_context():
    preference.check_context()
    if context.temp_status != "good" or context.humidity_status != "good":
        noti_body = context.get_context_message()
        if context.temp_status.find("too") == -1 and context.humidity_status.find("too") == -1:
            if preference.comfortable_status == True:
                PushBullet.send_notification("From Raspberry Pi", noti_body)
                preference.comfortable_status = False
        else:
            PushBullet.send_notification("From Raspberry Pi", noti_body)
    
def reset():
    if (datetime.datetime.now().strftime("%H:%M") == "11:16"):
        if (preference.comfortable_status == True):
            push_last_noti()
        else:
            preference.comfortable_status = True

def push_last_noti():
    noti_body = "Average temperature of the day: " + get_avg_temp() + " Celsius"
    noti_body += "\nAverage humidity of the day: " + get_avg_humidity() + " %"
    noti_body += "\nSee you tomorrow! Good night"
    PushBullet.send_notification("From Raspberry Pi", noti_body)

def get_avg_temp():
    try:
        return str(round(Database.execute_equation(
            "AVG(temp)",
            " WHERE timestamp >= date('now','-1 day')"
        ), 2))
    except:
        print("Fail to get average temperature")
        sys.exit()

def get_avg_humidity():
    try:
        return str(round(Database.execute_equation(
            "AVG(humidity)",
            " WHERE timestamp >= date('now','-1 day')"
        ), 2))
    except:
        print("Fail to get average humidity")
        sys.exit()

def save_status():
    json_content = {
        "comfortable_status" : preference.comfortable_status,
        "create_new_table" : preference.create_new_table
    }
    File.write_json(preference.status_file_name, json_content)

def evaluate_context():
    start_program()
    get_context_sense_hat()
    check_context()
    reset()
    save_status()
