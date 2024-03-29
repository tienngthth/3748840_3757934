#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
from createReport import start_creating_report

data_send = None

# Function to call GET API to get the latest context from the database
def test_get_api():
    resp = requests.get('http://127.0.0.1:8080/get/newest/context')
    if str(resp.content).find("Fail") != -1:
        print(resp.content)
    else:
        print(resp.json())

# Test different scenarios when uploading new context to database via POST API
def test_upload_api():
    test_upload_api_missing_argument()
    test_upload_api_invalid_number()
    test_upload_api_invalid_json()
    test_upload_api_successfully()

def test_upload_api_successfully():
    global data_send
    data_send = {"temp": 22, "humidity": 30}
    upload_api()

def test_upload_api_missing_argument():
    global data_send
    data_send = {"humidity": 30}
    upload_api()

def test_upload_api_invalid_number():
    global data_send
    data_send = {"temp": "22bc", "humidity": 30}
    upload_api()

def test_upload_api_invalid_json():
    global data_send
    data_send = 2
    upload_api()

# Function to call PUT API to upload new context from the database
def upload_api():
    resp = requests.post(
        'http://127.0.0.1:8080/upload/context',
        data = json.dumps(data_send),
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    )
    print(resp.content)
    # Call function to get the latest context and check if its uploaded as required, test GET API at the same time
    if str(resp.content).find("Successfully") != -1:
        test_get_api()
    
def test_update_api():
    test_update_api_invalid_json()
    test_update_api_invalid_number()
    test_update_api_one_argument()
    test_date_api_successfully()
    # Call function to get the latest context and check if its uploaded as required, test GET API at the same time
    test_get_api()

def test_date_api_successfully():
    global data_send
    data_send = {"temp": 25, "humidity": 35}
    update_api()

def test_update_api_one_argument():
    global data_send
    data_send = {"humidity": 35}
    update_api()

def test_update_api_invalid_number():
    global data_send
    data_send = {"temp": "22bc", "humidity": 30}
    update_api()

def test_update_api_invalid_json():
    global data_send
    data_send = 2
    update_api()

# Function to call PUT API to update the latest context from the database
def update_api():
    resp = requests.put(
        'http://127.0.0.1:8080/update/newest/context',
        data = json.dumps(data_send),
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    )
    print(resp.content)
        
if __name__ == "__main__":
    try:
        test_upload_api()
        test_update_api()
    except:
        # Print error if can not connect to server
        print("Can not connect to server")
