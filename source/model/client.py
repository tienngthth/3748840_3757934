# import bluetooth

# class Client:
#     sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#     def __init__(bluetooth_address, port):
#         self.port = port
#         self.bluetooth_address = bluetooth_address

#     def open_socket():
#         sock.connect((bd_addr, port))

#     def send_message(message)
#         sock.send(message)

#     def close_socke():
#         sock.close()

import bluetooth

bd_addr = "DC:A6:32:4A:0C:41"

client_port = 1
server_port =2
server_sock.bind(("",server_port))
server_sock.listen(1)

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, client_port))

client_sock,address = server_sock.accept()
print ("Accepted connection from [{}]".format(address))

sock.send("hello!!")

sock.close()