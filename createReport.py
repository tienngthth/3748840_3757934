"""
(4)	Create a python file called createReport.py which will create a csv file called report.csv. 
This file should contain a separate row for each days’ data, additionally this data resides in the 
database. 
If each piece of data is within the configured comfort temperature range then the status of OK is 
applied, otherwise the label of BAD is applied. An appropriate message detailing the error(s) is 
included.

This script is executed manually to generate the report.
to record your data every day I suggest that you just record the last hour per day, 
I means set the system to 11pm then that is the last data you will record per day.
"""
from model.preference import Preference
from model.database import Database
from model.fileHandle import File

def record_data():
    last_record = Database.select_a_record("*",  "SENSEHAT_data", " ORDER BY timestamp DESC LIMIT 1")
    File.write_json("report.csv", last_record)