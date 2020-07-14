import sqlite3 
import json
import requests
import datetime
import sys
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
dbname = "sensehat.db"
token ="o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj"
con = sqlite3.connect('sensehat.db')
    
class Preference:
    def __init__(self, cold_max, comfortable_min, comfortable_max, hot_min):
        self.cold_max = cold_max
        self.comfortable_min = comfortable_min                
        self.comfortable_max = comfortable_max
        self.hot_min = hot_min
        self.comfortable_status = True
    
    def check_comfortable(self, temp):
        if temp > self.comfortable_max:
            self.set_comfortable_status(False)
            return "hot"
        elif temp < self.comfortable_min:
            self.set_comfortable_status(False)
            return "cold"
        else: 
            return "good"

    def set_comfortable_status(self, status):
        self.comfortable_status = status

class Context:
    def __init__(self, temp, humidity):
        self.time = datetime.datetime.now()
        self.temp = round(temp, 2)                
        self.humidity = round(humidity, 2)    
    
def create_db():
    with con: 
        cur = con.cursor() 
        cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
        cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")

def read_config():
    try:
        config_file = open("config.json")
        parse_json(json.load(config_file)) 
    except:
        send_notification_via_pushbullet("From Raspberry Pi", "Config file error")
        sys.exit()

def parse_json(config_json):
    cold_max = float(config_json["cold_max"])
    comfortable_min = float(config_json["comfortable_min"])
    comfortable_max = float(config_json["comfortable_max"])
    hot_min = float(config_json["hot_min"])
    global preference
    preference = Preference (cold_max, comfortable_min, comfortable_max, hot_min)
         
def get_context_sense_hat():    
    global context
    context = Context(sense.get_temperature(), sense.get_humidity())
    log_data_to_db(context)

def log_data_to_db(context):    
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute(
        "INSERT INTO SENSEHAT_data values((?), (?), (?))", 
        (context.time, context.temp, context.humidity)
    ) 
    conn.commit()
    conn.close()
    display_db()

def display_db():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()  

def check_context():
    status = preference.check_comfortable(context.temp)
    if status != "good" and preference.comfortable_status == True:
        body = "Temperature is too {}: {} celcius".format(status, context.temp)
        send_notification_via_pushbullet("From Raspberry Pi", body)

def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body} 
    resp = requests.post(
        'https://api.pushbullet.com/v2/pushes', 
        data=json.dumps(data_send),
        headers={'Authorization': 'Bearer ' + token, 
        'Content-Type': 'application/json'}
    )
    if resp.status_code != 200:
        raise Exception('something wrong')
    else:
        print('complete sending')

def main():
    create_db()
    read_config()
    while True:        
        get_context_sense_hat()
        check_context()
        if (datetime.datetime.now().strftime("%H") == "00"):
            preference.set_comfortable_status(True)
        sleep(60)
        
main()
