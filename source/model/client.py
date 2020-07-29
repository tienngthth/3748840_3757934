import sys]
import bluetooth

class Client_socket:
   sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

   def __init__(bluetooth_address, port):
      self.port = port
      self.bluetooth_address = bluetooth_address

   def open_socket():
      sock.connect((bd_addr, port))

   def send_message(message)
      sock.send(message)

   def receive_message()
      return sock.recv(1024).decode('UTF-8')

   def close_socket():
      sock.close()