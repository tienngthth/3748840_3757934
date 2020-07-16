import requests
import json

class PushBullet:
    token = "o.FrPitNnEo4UJXz941zfjmUKNxKv9bGQj"
    
    @staticmethod
    def send_notification(title, body):
        data_send = {"type": "note", "title": title, "body": body}
        resp = requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data = json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + PushBullet.token,
            'Content-Type': 'application/json'}
        )
        if resp.status_code != 200:
            raise Exception('something wrong')
        else:
            print('complete sending')
