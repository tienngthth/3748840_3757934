import sys
from pushBullet import PushBullet
from fileHandle import File

class Preference:
    cold_max = None
    comfortable_min = None
    comfortable_max = None
    hot_min = None
    comfortable_status = None
    create_new_table = None

    @staticmethod
    def read_preference():
        try:
            config_json = File.read_json("config.json")
            status_json = File.read_json("status.json")
            Preference.parse_json(config_json, status_json)
        except:
            PushBullet.send_notification("From Raspberry Pi", "Fail to read files")
            sys.exit()

    @staticmethod
    def parse_json(config_json, status_json):
        Preference.set_preference (
            float(config_json["cold_max"]),
            float(config_json["comfortable_min"]),
            float(config_json["comfortable_max"]),
            float(config_json["hot_min"]),
            status_json["comfortable_status"],
            status_json["create_new_table"]
    )

    @staticmethod
    def set_preference(
        cold_max, comfortable_min, 
        comfortable_max, hot_min, 
        comfortable_status, create_new_table
    ):
        Preference.cold_max = cold_max
        Preference.comfortable_min = comfortable_min
        Preference.comfortable_max = comfortable_max
        Preference.hot_min = hot_min
        Preference.comfortable_status = comfortable_status
        Preference.create_new_table = create_new_table
   
    @staticmethod
    def set_comfortable_status(comfortable_status):
        Preference.comfortable_status = comfortable_status

    @staticmethod
    def check_comfortable(temp):
        if temp > Preference.comfortable_max:
            return "hot"
        elif temp < Preference.comfortable_min:
            return "cold"
        else:
            return "good"