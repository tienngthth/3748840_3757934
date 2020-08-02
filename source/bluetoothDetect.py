#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bluetooth
from time import sleep
from model.senseHat import PiSenseHat
from model.pushBullet import PushBullet

# Search for device containing keyword
def start_searching(server_name = "CuongvTien"):
   stop = False
   # Loop until joy stick is pressed or a device is detected
   while not stop:
      # Wait until bluetooth is on and stable
      try:
         sleep(5)
         # Get all nearby devices mac address
         nearby_devices = bluetooth.discover_devices()
         nearby_devices_mac_address = []
         # Loop through all nearby devices
         for server_mac_address in nearby_devices:
            # Get the device name from its mac address
            device_name = str(bluetooth.lookup_name(server_mac_address, timeout = 5))
            # Check if a device name contains the required key word
            if device_name.find(server_name) != -1:
               nearby_devices_mac_address.append(device_name + ": " + server_mac_address)
         # Inform that no device is detected
         if len(nearby_devices_mac_address) == 0:
            PushBullet.send_notification("Can not detect nearby devices with CuongvTien key word")
         else:
            message = ""
            # Loop through all matched devices to create a notification message
            for address in nearby_devices_mac_address:
               message += ( address + "\n")
            # Send a list of matched devices' names and addresses
            PushBullet.send_notification(message)
            stop = True
         # Detect stick pressed to stop finding bluetooth device
         if PiSenseHat.detect_stick():
            stop = True
      except:
         start_searching()

if __name__ == "__main__":
    start_searching()