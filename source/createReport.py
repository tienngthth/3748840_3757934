#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from time import sleep
from model.fileHandle import File
from model.context import Context
from model.database import Database
from model.preference import Preference
from model.util import Util

def start_creating_report():
    global preference, context
    preference = Preference()
    context = Context()
    get_latest_context()
    preference.check_context(context)
    record_data()

def get_latest_context():
    if not preference.create_new_table:
        try:
            last_context = Database.select_a_record("*", " ORDER BY timestamp DESC LIMIT 1")
            context.update_context(last_context[1], last_context[2], last_context[0])
        except:
            print("Fail to get latest record from database")
            sys.exit()
    else:
        print("New table is not created. Please check config file and your database")
        sys.exit()

def record_data():
    print("Input context report file name. Default name is report.csv")
    File.write_csv(Util.get_file_name("report", ".csv"), context.get_context_report_record())
    print("last record reported")

if __name__ == "__main__":
    start_creating_report()


