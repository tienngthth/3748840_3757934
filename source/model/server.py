import bluetooth

class Server:
    HOST = ''
    PORT = 2
    client = None

    def __init__(self):
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.bind((HOST, PORT))
        socket.listen(1)

    def connect(self):
        client, addr = socket.accept()

    def send_message(self, message):
        client.send(message)

    def recveive_message(self):
        return socket.recv

