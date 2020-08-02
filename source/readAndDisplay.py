#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time
from model.senseHat import PiSenseHat, blu, gre, red, whi
from model.preference import Preference
from model.database import Database
from model.context import Context
from monitorAndNotify import evaluate_context

def start_read_and_display_program():
    global preference, context
    preference = Preference()
    context = Context()
    # Get latest context from the database and evaluate the context and display to Sense HAT
    get_latest_context()
    preference.check_context(context)
    display_context()

def get_latest_context():
    try:
        last_context = Database.select_a_record("temp, humidity", " ORDER BY timestamp DESC LIMIT 1")
        context.update_context(last_context[0], last_context[1])
    except:
        PiSenseHat.raise_error("Fail to get latest record from database")

# Display context to Sense HAT for 1 minute or when joy stick is pressed
def display_context():
    end = time() + 40
    stop = False
    while time() < end and not stop:
        display_temp()
        display_humidity()
        # Stop display context when joy stick pressed is detected
        if PiSenseHat.detect_stick():
            stop = True
    PiSenseHat.show_letter("*")

# Display temperature with appropriate color to Sense HAT
def display_temp():
    if context.temp_status.find("cold") != -1:
        PiSenseHat.show_message(context.to_string_temp(), blu)
    elif context.temp_status.find("hot")  != -1:
        PiSenseHat.show_message(context.to_string_temp(), red)
    else:
        PiSenseHat.show_message(context.to_string_temp(), gre)

# Display humidity with appropriate color to Sense HAT
def display_humidity():
    if context.humidity_status.find("dry")  != -1:
        PiSenseHat.show_message(context.to_string_humidity(), blu)
    elif context.humidity_status.find("humid")  != -1:
        PiSenseHat.show_message(context.to_string_humidity(), red)
    else:
        PiSenseHat.show_message(context.to_string_humidity(), gre)

if __name__ == "__main__":
    # Call monitor and notify solution
    evaluate_context()
    # Start the read and display solution
    start_read_and_display_program() 