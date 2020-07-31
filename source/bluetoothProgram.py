#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from model.client import Client
from model.server import Server
from model.context import Context

def evaluate_current_context():
    global preference, context
    preference = Preference()
    context = Context()
    send_current_context()
    while True:
        sticks = PiSenseHat.detect_sticks()
        if sticks > 1:
            server.send_message("Bye bye bye Pikatu")
            break
        else:
            send_current_context()

def send_current_context():
    context.update_context_real_time(False)
    preference.check_context(context)
    server.send_message(context.get_context_report_record())

def run_server():
    global server
    server = Server()
    server.accept_connection()
    evaluate_current_context()

def run_client():
    global client
    client = Client(server_name = "TienvCuong1", server_mac_address = "DC:A6:32:4A:0C:41")
    client.open_socket()
    while True:
        if client.retrieve_message.find("Bye") != -1:
            break

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
        client.close_socket()
    else:
        run_server()
        server.close_connection()

if __name__ == "__main__":
    start_connecting() 