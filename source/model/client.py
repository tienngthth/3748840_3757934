import sys
import bluetooth
import time

class ClientSocket:
   sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

   def __init__(self, bluetooth_address, port):
      self.__port = port
      self.bluetooth_address = bluetooth_address

   def open_socket(self):
      ClientSocket.sock.connect((bd_addr, self.__port))

   def send_message(self, message):
      ClientSocket.send(message)

   def receive_message(self):
      return ClientSocket.recv(1024).decode('UTF-8')

   def close_socket(self):
      ClientSocket.sock.close()

   # Search for device based on device's name
   def search(self, user_name, device_name):
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