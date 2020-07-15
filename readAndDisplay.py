#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time
from model.senseHat import SenseHat, blu, gre, red
from model.preference import Preference
from model.database import Database

def get_latest_temp():
    global temp
    row = Database.select_a_record("temp",  "SENSEHAT_data", " ORDER BY timestamp DESC LIMIT 1")
    print(row)
    temp = row[0]

def display_temp():
    if Preference.check_comfortable(temp) == "cold":
        SenseHat.show_message(str(temp) + " Celcius", blu)
    elif Preference.check_comfortable(temp) == "hot":
        SenseHat.show_message(str(temp) + " Celcius", red)
    else:
        SenseHat.show_message(str(temp) + " Celcius", gre)

def main():
    Preference.read_preference()
    Database.display_db()
    get_latest_temp()
    end = time() + 60
    while time() < end:
        display_temp()

main()