import bluetooth
import socket
from .util import Util

class Server:
    def __init__(self, host = '', port = 5):
        self.__socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.__set_up_connection(host, port)
        self.__connection = None

    def __set_up_connection(self, host, port):
        # try:
        # self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 5)
        self.__socket.bind((host, port))
        # except:
            # Util.raise_error("This port is occupied. Please try with another port") 
        self.__socket.listen(1) 
        print("Listenning...")  

    def accept_connection(self):
        self.__connection, addr = self.__socket.accept()

    def send_message(self, message):
        self.__connection.send(message)

    def retrieve_message(self):
        return self.__socket.recv(1024).decode('UTF-8')

    def close_connection(self):
      self.__connection.close() 

