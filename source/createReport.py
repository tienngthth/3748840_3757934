#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from model.fileHandle import File
from model.context import Context

def get_file_name():
    file_name = File.get_file_name()
    if file_name == None:
        file_name = "report"
    return file_name + ".csv"

def record_data():
    File.write_csv(get_file_name(), Context.get_context_report_record())
    print("last record reported")

