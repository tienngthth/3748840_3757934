#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time
from model.senseHat import SenseHat, blu, gre, red, whi
from model.preference import Preference
from model.database import Database
from monitorAndNotify import evaluate_context

def get_latest_temp():
    global temp
    row = Database.select_a_record("temp",  "SENSEHAT_data", " ORDER BY timestamp DESC LIMIT 1")
    temp = row[0]

def set_sense_hat():
    if Preference.check_comfortable(temp) == "cold":
        SenseHat.show_message(str(temp) + " Celsius", blu)
    elif Preference.check_comfortable(temp) == "hot":
        SenseHat.show_message(str(temp) + " Celsius", red)
    else:
        SenseHat.show_message(str(temp) + " Celsius", gre)

def main():
    evaluate_context()
    get_latest_temp()
    end = time() + 52
    stop = False
    while time() < end and not stop:
        set_sense_hat()
        if SenseHat.detect_stick():
            stop = True
    SenseHat.show_letter("*")

main()