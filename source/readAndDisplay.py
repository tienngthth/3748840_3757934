#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time
from model.senseHat import PiSenseHat, blu, gre, red, whi
from model.preference import Preference
from model.database import Database
from model.context import Context
from monitorAndNotify import evaluate_context

def get_latest_context():
    last_context = Database.select_a_record("*", " ORDER BY timestamp DESC LIMIT 1")
    Context.update_context(last_context[0], last_context[1], last_context[2])

def display_temp():
    if Context.temp_status.find("cold") != -1:
        PiSenseHat.show_message(Context.to_string_temp(), blu)
    elif Context.temp_status.find("hot")  != -1:
        PiSenseHat.show_message(Context.to_string_temp(), red)
    else:
        PiSenseHat.show_message(Context.to_string_temp(), gre)

def display_humidity():
    if Context.humidity_status.find("dry")  != -1:
        PiSenseHat.show_message(Context.to_string_humidity(), blu)
    elif Context.humidity_status.find("humid")  != -1:
        PiSenseHat.show_message(Context.to_string_humidity(), red)
    else:
        PiSenseHat.show_message(Context.to_string_humidity(), gre)

def main():
    evaluate_context()
    get_latest_context()
    Preference.check_context()
    end = time() + 40
    stop = False
    while time() < end and not stop:
        display_temp()
        display_humidity()
        if PiSenseHat.detect_stick():
            stop = True
    PiSenseHat.show_letter("*")

if __name__ == "__main__":
    main()