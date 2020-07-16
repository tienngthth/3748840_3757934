import json
import bluetooth
import datetime
import sys
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
connect_status = False

class Preference:
    def __init__(self, file):
        self.file = file

    # display database data
    def parse_json(self, config_json):
        global cold_max, hot_min, comfortable_max, comfortable_min
        cold_max = float(config_json["cold_max"])
        comfortable_min = float(config_json["comfortable_min"])
        comfortable_max = float(config_json["comfortable_max"])
        hot_min = float(config_json["hot_min"])

    def read_config(self):
        try:
            config_file = open("config.json")
            self.parse_json(json.load(config_file)) 
        except:
            print("File Config Error")
            sys.exit()


class Bluetooth:
    def check_context():
        context = Context()
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
        resp = requests.post(
            'https://api.pushbullet.com/v2/pushes', 
            data=json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + token, 
            'Content-Type': 'application/json'}
        )
        if resp.status_code != 200:
            raise Exception('something wrong')

    # Search for device based on device's name
    def search(user_name, device_name):
        while True:
            device_address = None
            dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
            print("\nCurrently: {}".format(dt))
            time.sleep(3) #Sleep three seconds 
            nearby_devices = bluetooth.discover_devices()

            for mac_address in nearby_devices:
                if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                    device_address = mac_address
                    break
            if device_address is not None:
                print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
                sense = SenseHat()
                temp = round(sense.get_temperature(), 1)
                sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
            else:
                print("Could not find target device nearby...")