#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from model.client import Client
from model.server import Server
from model.context import Context
from model.preference import Preference
from model.senseHat import PiSenseHat
from model.util import Util

# Function to call when Pi is a server
def run_server():
    global server
    server = Server()
    evaluate_current_context()

# Evaluate context to send to client when needed
def evaluate_current_context():
    global preference, context
    preference = Preference()
    context = Context()
    # Send context message first time after connection established
    evaluate_and_send_context()
    while True:
        pressed = PiSenseHat.detect_stick_middle()
        # Send good bye message and close connection if joy stick is pressed in the middle
        if pressed == "middle":
            server.send_message("Bye bye bye client")
            server.close_connection()
            break
        # Send context message every joy stick is pressed left, right, up, down
        elif pressed == "pressed":
            evaluate_and_send_context()

# Get, evaluate context and send to client
def evaluate_and_send_context():
    context.update_real_time_context(False)
    preference.check_context(context)
    server.send_message(context.get_context_report_record())

# Function to call when Pi is a client
def run_client():
    # Ask for user input server name
    promt_name_message = "Input server name. Default name is CuongvTien"
    server_name = Util.get_user_input("CuongvTien", promt_name_message)
    # Ask for user input mac address
    promt_mac_message = "Input server mac address. Default mac address is DC:A6:32:4A:0C:41"
    server_mac_address = Util.get_user_input("DC:A6:32:4A:0C:41", promt_mac_message)
    # Create new client with target server name or server mac address
    client = Client(server_name = server_name, server_mac_address = server_mac_address)
    while True:
        # Constantly display message received from server until the end of connection (receive good bye message)
        message = client.retrieve_message()
        if message.find("Bye") != -1:
            print(message)
            # Close socket after connection is closed
            client.close_socket()
            break
        else:
            print(message)

# Validate input role, only accept client or server
def set_up_role():
    role = input("This pi is a (client/server): ")
    while role != "client" and role != "server":
        print("Invalid role input")
        role = input("This pi is a (client/server): ")
    return role

# Get role of the pi - client or server
def start_connecting():
    role = set_up_role()
    if role == "client":
        run_client()
    else:
        run_server()

if __name__ == "__main__":
    start_connecting() 