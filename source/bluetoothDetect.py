#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bluetooth
from time import sleep
from model.pushBullet import PushBullet

# Search for device based on device's name
def start_searching(server_name = "CuongvTien"):
   for i in (0, 5):
      sleep(3) #Sleep three seconds 
      nearby_devices = bluetooth.discover_devices()
      nearby_devices_mac_address = []
      for server_mac_address in nearby_devices:
            if str(bluetooth.lookup_name(server_mac_address, timeout = 5)).find(server_name) != -1:
               nearby_devices_mac_address.append(server_name + ": " + server_mac_address)
      if len(nearby_devices_mac_address) == 0:
         PushBullet.raise_error("From Raspberry Pi", "Can not detect nearby devices with CuongvTien key word")
      else:
         PushBullet.send_notification("From Raspberry Pi", nearby_devices_mac_address)

if __name__ == "__main__":
    start_searching() 