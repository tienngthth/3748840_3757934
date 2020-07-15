"""
(3)	Create a python file called readAndDisplay.py which will retrieve the newest temperature record from
the database and display the temperature in LED matrix on Sense HAT. The LED light should be refreshed 
every minute.
1.	If the level of temperature is cold, display temperature with blue colour.
2.	If the level of temperature is comfortable, display temperature with green colour.
3.	If the level of temperature is hot, display temperature with red colour.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
import requests
import datetime
import sys
import pathlib
from sense_hat import SenseHat
from time import sleep
from ultility import blu, gre, red
from model.preference import Preference

sense = SenseHat()

def get_latest_temp():
    global temp
    conn = sqlite3.connect("sensehat.db")
    curs = conn.cursor()
    print ("\nEntire database contents:\n") 
    for row in curs.execute("SELECT * FROM SenseHat_data ORDER BY ID DESC LIMIT 1"):
        temp = row[1, len(row - 1)]
    conn.close()

def display_temp():
    if temp < Preference.comfortable_min:
        sense.show_message(temp, text_colour = blu)
    elif temp > Preference.comfortable_max:
        sense.show_message(temp, text_colour = red)
    else:    
        sense.show_message(temp, text_colour = gre)

def main():
    get_latest_temp()
    display_temp()

main()