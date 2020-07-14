import sqlite3 
import json
import requests
import datetime
import sys
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
dbname = "sensehat.db"
ACCESS_TOKEN="o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj"
comfortable_status = True
con = sqlite3.connect('sensehat.db')

with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
    
class Context:
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        self.logDataToDB()
    
    def logDataToDB(self):    
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        curs.execute(
            "INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", 
            (self.temp, self.humidity)
        ) 
        # parameterized
        conn.commit()
        conn.close()
        self.displayData()
    
    def displayData(self):
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SenseHat_data"):
            print (row)
        conn.close()  
    
# display database data
def read_config():
    try:
        config_file = open("config.json")
        parse_json(json.load(config_file)) 
    except:
        send_notification_via_pushbullet("From Raspberry Pi", "Config file error")
        sys.exit()

def parse_json(config_json):
    global cold_max, hot_min, comfortable_max, comfortable_min
    cold_max = float(config_json["cold_max"])
    comfortable_min = float(config_json["comfortable_min"])
    comfortable_max = float(config_json["comfortable_max"])
    hot_min = float(config_json["hot_min"])
         
def get_context_sense_hat():    
    global context
    sense.clear()
    temp = round(sense.get_temperature(), 2)
    sense.clear()
    humidity = round(sense.get_humidity(), 2)
    context = Context(temp, humidity)

def check_context():
    global comfortable_status
    body = "Good"
    if context.temp > comfortable_max:
        body = "Temperature is too hot: {} celcius"
    elif context.temp < comfortable_min:
        body = "Temperature is too cold: {} celcius "
    if body != "Good" and comfortable_status == True:
        body = body.format(context.temp)
        send_notification_via_pushbullet("From Raspberry Pi", body)
        comfortable_status = False

def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body} 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                        headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                        'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('something wrong')
    else:
        print('complete sending')

def main():
    global comfortable_status
    read_config()
    while True:        
        get_context_sense_hat()
        check_context()
        if (datetime.datetime.now().strftime("%H") == "00"):
            comfortable_status = True
        sleep(2)
        
main()
