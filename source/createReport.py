#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from model.fileHandle import File
from model.context import Context
from model.database import Database
from model.preference import Preference
from model.util import Util

def get_latest_context():
    if not Preference.create_new_table:
        last_context = Database.select_a_record("*", " ORDER BY timestamp DESC LIMIT 1")
        Context.update_context(last_context[0], last_context[1], last_context[2])
    else:
        print("New table is not created. Please check config file and your database")

def record_data():
    get_latest_context()
    Preference.read_preference()
    Preference.check_context()
    File.write_csv(Util.get_file_name("report"), Context.get_context_report_record())
    print("last record reported")

record_data()

