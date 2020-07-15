#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from time import time
from model.senseHAT import SenseHat, blu, gre, red
from model.preference import Preference
from model.database import Database

def get_latest_temp():
    global temp
    for row in Database.select_record("*",  "SenseHat_data", " ORDER BY ID DESC LIMIT 1"):
        temp = row[1, len(row - 1)]

def display_temp():
    if temp < Preference.comfortable_min:
        SenseHat.show_message(temp + "Celcius", blu)
    elif temp > Preference.comfortable_max:
        SenseHat.show_message(temp + "Celcius", red)
    else:    
        SenseHat.show_message(temp + "Celcius", gre)

def main():
    Preference.read_preference()
    get_latest_temp()
    end = time() + 60
    while time() < end:
        display_temp()

main()