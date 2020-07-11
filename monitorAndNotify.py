# import sqlite3
import json
# import requests
import datetime
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
dbname = "AA"
ACCESS_TOKEN=""
comfortable_status = True
cold_max = "0"
comfortable_min = "15"
comfortable_max = "25"
hot_min = "50"

class Context:
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        # self.logDataToDB()
    
    # def logDataToDB(self):	
    #     conn=sqlite3.connect(dbname)
    #     curs=conn.cursor()
    #     curs.execute(
    #         "INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", 
    #         (self.temp, self.humidity)
    #     ) 
    #     # parameterized
    #     conn.commit()
    #     conn.close()

def read_config():
    try:
        config_file = open("config.json")
        parse_json(json.load(config_file))
    except:
        print("missing config file")

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
    global comfortable_status
    body = "Good"
    if context.temp > float(comfortable_max):
        body = "Temperature is too hot: {} celcius"
    elif context.temp < float(comfortable_min):
        body = "Temperature is too cold: {} celcius "
    if body != "Good" and comfortable_status == True:
        body = body.format(context.temp)
        # send_notification_via_pushbullet("From Raspberry Pi", body)
        comfortable_status = False

# def send_notification_via_pushbullet(title, body):
#     data_send = {"type": "note", "title": title, "body": body} 
#     resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
#                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
#                         'Content-Type': 'application/json'})
#     if resp.status_code != 200:
#         raise Exception('something wrong')
#     else:
#         print('complete sending')

def main():
    global comfortable_status
    while True:
        read_config()
        get_context_sense_hat()
        check_context()
        if (datetime.datetime.now().strftime("%H") == "00"):
            comfortable_status = True
        sleep(60)
        
main()
