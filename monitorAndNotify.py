from sense_hat import SenseHat
import sqlite3
import json
import requests
import datetime

sense = SenseHat()
dbname = "AA"
ACCESS_TOKEN=""
comfortable_status = True
cold_max = ""
comfortable_min = ""
comfortable_max = ""
hot_min = ""

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

def read_config():
    try:
        config_file = open("config.json")
    except:
        print("An exception occurred")
    parse_json(json.load(config_file))

def parse_json(config_json):
    cold_max = config_json["cold_max"]
    comfortable_min = config_json["comfortable_min"]
    comfortable_max = config_json["comfortable_max"]
    hot_min = config_json["hot_min"]

def get_context_sense_hat():	
    global context
    sense.clear()
    temp = sense.get_temperature()
    sense.clear()
    humidity = sense.get_humidity()
    context = Context(temp, humidity)

def check_context():
    body = "Good"
    if context.temp > comfortable_max:
        body = "Temperature too hot: " + context.temp
    elif context.temp < comfortable_min:
        body = "Temperature too cold: " + context.temp
    if body != "Good" and comfortable_status == True:
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
    while True:
        read_config()
        get_context_sense_hat()
        check_context()
        if (datetime.datetime.now().strftime("%H") == "00"):
            comfortable_status = True
        sense.sleep(60)
        
main()
