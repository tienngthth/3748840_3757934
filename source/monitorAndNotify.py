#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
from model.preference import Preference
from model.context import Context
from model.pushBullet import PushBullet
from model.database import Database
from model.fileHandle import File
from model.util import Util

def start_evaluating_context():
    global preference, context
    preference = Preference()
    context = Context()
    # Get real time context from Sense HAT's sensors and evaluating the context
    get_context_sense_hat()
    check_context()

# Check to create new table, get the current context and log it to database
def get_context_sense_hat():
    # Check if creating new table is needed
    check_table()
    # Get the current context
    context.update_real_time_context()    

# Check if creating new table is needed
def check_table():
    if preference.create_new_table == True:
        try:
            Database.create_table(
                "(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)"
            )
            # Remember that the new table is created
            preference.create_new_table = False
        except:
            PushBullet.raise_error("Fail to create new database table")

# Check the current context and send notifications to user if needed
def check_context():
    preference.check_context(context)
    # Check to send appropriate message
    if context.temp_status != "good" or context.humidity_status != "good":
        noti_body = context.get_context_message()
        # Send context whenever it is dangerous 
        if context.temp_status.find("too") == -1 and context.humidity_status.find("too") == -1:
            # Only send uncomfortable context 1 per day
            if preference.comfortable_status == True:
                PushBullet.send_notification(noti_body)
                # Remember that 1 uncomfortable context has been sent
                preference.comfortable_status = False
        else:
            PushBullet.send_notification(noti_body)
    
# Check for the end of the day
def reset():
    if (datetime.datetime.now().strftime("%H:%M") == "23:59"):
        if (preference.comfortable_status == True):
            # Push last notification with average temperature and humidity if it is a good day
            push_last_noti()
        else:
            # Reset the uncomfortable status flag for a new day
            preference.comfortable_status = True

# Push last notification with average temperature and humidity if it is a good day
def push_last_noti():
    noti_body = "Today is a good day\n"
    noti_body += "Average temperature of the day: " + get_avg_temp() + " Celsius"
    noti_body += "\nAverage humidity of the day: " + get_avg_humidity() + " %"
    noti_body += "\nSee you tomorrow! Good night"
    PushBullet.send_notification(noti_body)

# Get average temperature
def get_avg_temp():
    try:
        return str(round(Database.execute_equation(
            "AVG(temp)",
            " WHERE timestamp >= date('now','-1 day')"
        ), 2))
    except:
        PushBullet.send_notification("Fail to get average temperature")
        return 0.00

# Get average humidity
def get_avg_humidity():
    try:
        return str(round(Database.execute_equation(
            "AVG(humidity)",
            " WHERE timestamp >= date('now','-1 day')"
        ), 2))
    except:
        PushBullet.send_notification("Fail to get average humidity")
        return 0.00

# Save the adjusted status back to file
def save_status():
    json_content = {
        "comfortable_status" : preference.comfortable_status,
        "create_new_table" : preference.create_new_table
    }
    File.write_json(preference.status_file_name, json_content)

def evaluate_context():
    start_evaluating_context()
    reset()
    save_status()
