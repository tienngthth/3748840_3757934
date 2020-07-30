import bluetooth

class Server:
    HOST = ''
    PORT = 2
    client = None
    def __init__():
        socket= bluetooth.BluetoothSocket(bluetooth.RFCOMM )
        socket.bind((HOST, PORT))
        socket.listen(1)

    def connect():
        client, addr = socket.accept()

    def send_message(message):
        client.send(message)

    def recveive_message():
        return socket.recv

