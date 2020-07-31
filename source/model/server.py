import bluetooth

class Server:
    def __init__(self, host, port):
        self.__socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.__socket.bind((host, port))
        self.__socket.listen(1)
        self.__connection = None

    def accept_connection(self):
        self.__connection, addr = self.__socket.accept()

    def send_message(self, message):
        self.__connection.send(message)

    def retrieve_message(self):
        return self.__socket.recv(1024).decode('UTF-8')

    def close_connection(self):
      self.__connection.close() 

