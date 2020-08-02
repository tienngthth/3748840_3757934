import requests
import json
import sys
from .util import Util

class PushBullet:
    # "o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj",
    tokens = ("o.SiF4IfG8yQGsTkRveEkYGRIvtQxz7udq", )
    
    @staticmethod
    def send_notification(body, title = "From Raspberry Pi", tokens = None):
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
                Util.raise_error("Fail to send push bullet")

    @staticmethod
    def raise_error(body, title = "From Raspberry Pi", tokens = None):
        PushBullet.send_notification(body, title, tokens)
        sys.exit()
