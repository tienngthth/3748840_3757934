#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from model.fileHandle import File
from model.context import Context
from model.database import Database
from model.preference import Preference

def get_latest_context():
    if not Preference.create_new_table:
        last_context = Database.select_a_record("*", " ORDER BY timestamp DESC LIMIT 1")
        Context.update_context(last_context[0], last_context[1], last_context[2])
    else:
        print("New table is not created. Please check config file and your database")

def get_file_name():
    file_name = File.get_file_name()
    if file_name == None:
        file_name = "report"
    return file_name + ".csv"

def record_data():
    get_latest_context()
    Preference.read_preference()
    Preference.check_context()
    File.write_csv(get_file_name(), Context.get_context_report_record())
    print("last record reported")

record_data()

