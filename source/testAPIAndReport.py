#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
from createReport import start_creating_report

def test_get_api():
    resp = requests.get('http://127.0.0.1:8080/get/newest/context')
    if str(resp.content).find("Fail") != -1:
        print(resp.content)
    else:
        print(resp.json())

def test_upload_api():
    data_send = {"temp": 22, "humidity": 30}
    resp = requests.post(
        'http://127.0.0.1:8080/upload/context',
        data = json.dumps(data_send),
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    )
    print(resp.content)
    test_get_api()

def test_update_api():
    data_send = {"humidity": 35}
    resp = requests.put(
        'http://127.0.0.1:8080/update/newest/context',
        data = json.dumps(data_send),
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    )
    print(resp.content)
    test_get_api()

if __name__ == "__main__":
    test_upload_api()
    test_update_api()
    start_creating_report()
