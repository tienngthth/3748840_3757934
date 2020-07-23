#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time
from model.senseHat import PiSenseHat, blu, gre, red, whi
from model.preference import Preference
from model.database import Database
from model.context import Context
from monitorAndNotify import evaluate_context

def get_latest_temp():
    global temp, humidity
    row = Database.select_a_record("temp, humidity",  "SENSEHAT_data", " ORDER BY timestamp DESC LIMIT 1")
    Context.temp = row[0]
    Context.humidity = row[1]

def display_temp():
    if (Context.temp_status.find("cold")):
        PiSenseHat.show_message(Context.to_string_temp, red)
    elif Context.temp_status.find("hot"):
        PiSenseHat.show_message(Context.to_string_temp, red)
    else:
        PiSenseHat.show_message(Context.to_string_temp, gre)

def display_humidity():
    if Context.humidity_status.find("dry"):
        PiSenseHat.show_message(Context.to_string_humidity, blu)
    elif Context.humidity_status.find("humid"):
        PiSenseHat.show_message(Context.to_string_humidity, red)
    else:
        PiSenseHat.show_message(Context.to_string_humidity, gre)

def main():
    evaluate_context()
    get_latest_temp()
    Preference.check_context()
    end = time() + 52
    stop = False
    while time() < end and not stop:
        display_temp()
        display_humidity()
        if PiSenseHat.detect_stick():
            stop = True
    PiSenseHat.show_letter("*")

main()