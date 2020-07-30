import json
import bluetooth
import datetime
import sys
from sense_hat import SenseHat
from time import sleep
from model.client import Client
from model.context import Context

sense = SenseHat()
connect_status = False

class Bluetooth:
    search()
    Context.update_context_real_time()
    Preference.check_context()
    noti_body = Context.get_context_message()
    Client.send_message(noti_body)

# # Search for device based on device's name
# def search(user_name, device_name):
#     while True:
#         device_address = None
#         dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
#         print("\nCurrently: {}".format(dt))
#         time.sleep(3) #Sleep three seconds 
#         nearby_devices = bluetooth.discover_devices()

#         for mac_address in nearby_devices:
#             if device_name == bluetooth.lookup_name(mac_address, timeout=5):
#                 device_address = mac_address
#                 break
#         if device_address is not None:
#             print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
#             sense = SenseHat()
#             temp = round(sense.get_temperature(), 1)
#             sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
#         else:
#             print("Could not find target device nearby...")