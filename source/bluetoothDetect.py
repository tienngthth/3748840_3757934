#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bluetooth
from model.pushBullet import PushBullet

# Search for device based on device's name
def start_searching(server_name = "CuongvTien"):
   nearby_devices = bluetooth.discover_devices()
   nearby_devices_mac_address = []
   for server_mac_address in nearby_devices:
         device_name = str(bluetooth.lookup_name(server_mac_address, timeout = 5))
         if device_name.find(server_name) != -1:
            nearby_devices_mac_address.append(device_name + ": " + server_mac_address)
   if len(nearby_devices_mac_address) == 0:
      PushBullet.raise_error("Can not detect nearby devices with CuongvTien key word")
   else:
      message = ""
      for address in nearby_devices_mac_address:
         message += ( address + "\n")
      PushBullet.send_notification(message)

if __name__ == "__main__":
    start_searching()