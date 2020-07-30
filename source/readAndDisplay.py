#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from time import time
from model.senseHat import PiSenseHat, blu, gre, red, whi
from model.preference import Preference
from model.database import Database
from model.context import Context
from monitorAndNotify import start_evaluating_context

def start_read_and_display_program():
    global preference, context
    preference = Preference()
    context = Context()
    get_latest_context()
    preference.check_context(context)
    display_context()

def get_latest_context():
    try:
        last_context = Database.select_a_record("temp, humidity", " ORDER BY timestamp DESC LIMIT 1")
        context.update_context(last_context[0], last_context[1])
    except:
        PiSenseHat.show_message("Fail to get latest record from database")
        sys.exit()

def display_temp():
    if context.temp_status.find("cold") != -1:
        PiSenseHat.show_message(context.to_string_temp(), blu)
    elif context.temp_status.find("hot")  != -1:
        PiSenseHat.show_message(context.to_string_temp(), red)
    else:
        PiSenseHat.show_message(context.to_string_temp(), gre)

def display_humidity():
    if context.humidity_status.find("dry")  != -1:
        PiSenseHat.show_message(context.to_string_humidity(), blu)
    elif context.humidity_status.find("humid")  != -1:
        PiSenseHat.show_message(context.to_string_humidity(), red)
    else:
        PiSenseHat.show_message(context.to_string_humidity(), gre)

def display_context():
    end = time() + 40
    stop = False
    while time() < end and not stop:
        display_temp()
        display_humidity()
        if PiSenseHat.detect_stick():
            stop = True
    PiSenseHat.show_letter("*")

if __name__ == "__main__":
    start_evaluating_context()
    start_read_and_display_program() 