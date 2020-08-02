#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from model.client import Client
from model.server import Server
from model.context import Context
from model.preference import Preference
from model.senseHat import PiSenseHat
from model.util import Util

def run_server():
    global server
    server = Server()
    evaluate_current_context()

def evaluate_current_context():
    global preference, context
    preference = Preference()
    context = Context()
    send_current_context()
    while True:
        pressed = PiSenseHat.detect_stick_middle()
        if pressed == "middle":
            server.send_message("Bye bye bye client")
            server.close_connection()
            break
        elif pressed == "pressed":
            send_current_context()
            
def send_current_context():
    context.update_real_time_context(False)
    preference.check_context(context)
    server.send_message(context.get_context_report_record())

def run_client():
    promt_name_message = "Input server name. Default name is CuongvTien"
    server_name = Util.get_user_input("CuongvTien", promt_name_message)
    promt_mac_message = "Input server mac address. Default mac address is DC:A6:32:4A:0C:41"
    server_mac_address = Util.get_user_input("DC:A6:32:4A:0C:41", promt_mac_message)
    client = Client(server_name = server_name, server_mac_address = server_mac_address)
    while True:
        message = client.retrieve_message()
        if message.find("Bye") != -1:
            print(message)
            client.close_socket()
            break
        else:
            print(message)

def set_up_role():
    role = input("This pi is a (client/server): ")
    while role != "client" and role != "server":
        print("Invalid role input")
        role = input("This pi is a (client/server): ")
    return role

def start_connecting():
    role = set_up_role()
    if role == "client":
        run_client()
    else:
        run_server()

if __name__ == "__main__":
    start_connecting() 