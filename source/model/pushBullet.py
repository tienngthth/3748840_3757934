import requests
import json
import sys

class PushBullet:
    tokens = ("o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj", "o.JFcEzPeGuu4QDrahlJVunGgV0ZkL57rE")
    
    @staticmethod
    def send_notification(title, body, tokens = None):
        if tokens == None:
            tokens = PushBullet.tokens
        data_send = {"type": "note", "title": title, "body": body}
        for token in tokens:
            resp = requests.post(
                'https://api.pushbullet.com/v2/pushes',
                data = json.dumps(data_send),
                headers = {
                    'Authorization': 'Bearer ' 
                    + token,
                    'Content-Type': 'application/json'
                }
            )
            if resp.status_code != 200:
                print("Can not send push bullet")
                sys.exit() 
            else:
                print("complete sending")
