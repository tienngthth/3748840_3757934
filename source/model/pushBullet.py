import requests
import json

class PushBullet:
    tokens = ("", "")
    
    @staticmethod
    def send_notification(title, body, tokens = None):
        if tokens != None:
            PushBullet.tokens = tokens
        data_send = {"type": "note", "title": title, "body": body}
        for token in PushBullet.tokens:
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
                raise Exception('something wrong')
            else:
                print('complete sending')
