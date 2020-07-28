#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time
from model.senseHat import PiSenseHat, blu, gre, red, whi
from model.preference import Preference
from model.database import Database
from model.context import Context
from monitorAndNotify import evaluate_context

def get_latest_context():
    global temp, humidity
    row = Database.select_a_record("temp, humidity", " ORDER BY timestamp DESC LIMIT 1")
    Context.temp = row[0]
    Context.humidity = row[1]

<<<<<<< HEAD
def set_sense_hat():
    if Preference.check_comfortable(temp) == "cold":
        PiSenseHat.show_message(str(temp) + " Celsius", blu)
    elif Preference.check_comfortable(temp) == "hot":
        PiSenseHat.show_message(str(temp) + " Celsius", red)
    else:
        PiSenseHat.show_message(str(temp) + " Celsius", gre)
=======
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
>>>>>>> context

def main():
    evaluate_context()
    get_latest_context()
    Preference.check_context()
    end = time() + 52
    stop = False
    while time() < end and not stop:
<<<<<<< HEAD
        set_sense_hat()
=======
        display_temp()
        display_humidity()
>>>>>>> context
        if PiSenseHat.detect_stick():
            stop = True
    PiSenseHat.show_letter("*")

main()