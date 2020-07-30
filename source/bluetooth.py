import json
import bluetooth
import datetime
import sys
from time import sleep
from model.client import Client
from model.server import Server
from model.context import Context

sense = SenseHat()
connect_status = False

class Bluetooth:
    search()
    Context.update_context_real_time()
    Preference.check_context()
    noti_body = Context.get_context_message()
    Client.send_message(noti_body)

def run_server():

def run_client():


def start_connecting():
    pi = input("This pi is a (client/server): ")
    if pi == "client":
        run_client()
    else:
        run_server()

if __name__ == "__main__":
    start_connecting()