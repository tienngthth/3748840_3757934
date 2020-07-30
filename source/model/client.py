import bluetooth

class Client:

    bd_addr = "DC:A6:32:4A:0C:41"

    port = 1

    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))

    sock.send("hello!!")

    sock.close()