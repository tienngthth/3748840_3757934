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
    try:
        last_context = Database.select_a_record("*", " ORDER BY timestamp DESC LIMIT 1")
        context.update_context(last_context[1], last_context[2], last_context[0])
    except:
        Util.raise_error("Fail to get latest record from database, required table may not exist")

def record_data():
    message = "Input context report file name. Default name is report.csv"
    File.write_csv(Util.get_file_name("report", ".csv", message), context.get_context_report_record() + "--\n")

if __name__ == "__main__":
    start_creating_report()


