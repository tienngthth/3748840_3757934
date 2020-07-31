import sys
import bluetooth
import time
from .util import Util

class ClientSocket:

   def __init__(self, server_name, server_mac_address = None, port = 2):
      self.__port = port
      self.__find_server(server_name, server_mac_address)
      self.__socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

   def __find_server(server_name, server_mac_address):
      if server_mac_address is None and server_name is None:
         Util.raise_error("Please input server name or server mac address")
      if server_mac_address is not None and server_name is not None:
         print("Server mac addres is used")
      if server_mac_address is not None:
         self.__server_mac_address = server_mac_address
      else:
         self.__server_mac_address = self.__search(server_name)

   # Search for device based on device's name
   def search(self, server_name):
      for i in (0, 5):
         time.sleep(3) #Sleep three seconds 
         nearby_devices = bluetooth.discover_devices()

         for server_mac_address in nearby_devices:
               if server_name == bluetooth.lookup_name(server_mac_address, timeout=5):
                  return server_mac_address

      Util.raise_error("Can not detect specified nearby device")

   def open_socket(self):
      try:
         self.__socket.connect((self.__server_mac_address, self.__port))
      except:
         Util.raise_error("Can not connect to specified server")

   def send_message(self, message):
      self.__socket.send(message)

   def retrieve_message(self):
      return self.__socket.recv(1024).decode('UTF-8')

   def close_socket(self):
      self.__socket.close()
