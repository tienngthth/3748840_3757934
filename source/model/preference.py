import sys
from .fileHandle import File
from .context import Context
from .util import Util

class Preference:
    cold_max = None
    comfortable_min_temp = None
    comfortable_max_temp = None
    hot_min = None
    dry_max = None
    comfortable_min_humidity = None
    comfortable_max_humidity = None
    humid_min = None
    comfortable_status = None
    create_new_table = None

    @staticmethod
    def read_preference():
        config_json = File.read_json("config.json")
        status_json = File.read_json("status.json")
        Preference.parse_json(config_json, status_json)

    @staticmethod
    def parse_json(config_json, status_json):
        Preference.validate_config_preference(config_json)
        Preference.set_preference (
            float(config_json["cold_max"]),
            float(config_json["comfortable_min_temp"]),
            float(config_json["comfortable_max_temp"]),
            float(config_json["hot_min"]),
            float(config_json["dry_max"]),
            float(config_json["comfortable_min_humidity"]),
            float(config_json["comfortable_max_humidity"]),
            float(config_json["humid_min"]),
            status_json["comfortable_status"],
            status_json["create_new_table"]
    )

    @staticmethod
    def validate_config_preference(config_dict):
        for key, value in config_dict.items():
            if not Util.check_float(str(value)):
                print("Wrong " + key + " format - invalid number")
                sys.exit()
            
    @staticmethod
    def set_preference(
        cold_max, comfortable_min_temp, 
        comfortable_max_temp, hot_min, 
        dry_max, comfortable_min_humidity, 
        comfortable_max_humidity, humid_min, 
        comfortable_status, create_new_table
    ):
        Preference.cold_max = cold_max
        Preference.comfortable_min_temp = comfortable_min_temp
        Preference.comfortable_max_temp = comfortable_max_temp
        Preference.hot_min = hot_min
        Preference.dry_max = dry_max
        Preference.comfortable_min_humidity = comfortable_min_humidity
        Preference.comfortable_max_humidity = comfortable_max_humidity
        Preference.humid_min = humid_min
        Preference.comfortable_status = comfortable_status
        Preference.create_new_table = create_new_table
               

    @staticmethod
    def set_comfortable_status(comfortable_status):
        Preference.comfortable_status = comfortable_status

    @staticmethod
    def check_context():
        Preference.check_humidity()
        Preference.check_temp()

    @staticmethod
    def check_humidity():
        if Context.humidity > Preference.humid_min:
            Context.humidity_status = "too humid"
        elif Context.humidity > Preference.comfortable_max_humidity:
            Context.humidity_status = "humid"
        elif Context.humidity < Preference.dry_max:
            Context.humidity_status = "too dry"
        elif Context.humidity < Preference.comfortable_min_humidity:
            Context.humidity_status = "dry"
        else:
            Context.humidity_status = "good"

    @staticmethod
    def check_temp():
        if Context.temp > Preference.hot_min:
            Context.temp_status = "too hot"
        elif Context.temp > Preference.comfortable_max_temp:
            Context.temp_status = "hot"
        elif Context.temp < Preference.cold_max:
            Context.temp_status = "too cold"
        elif Context.temp < Preference.comfortable_min_temp:
            Context.temp_status = "cold"
        else:
            Context.temp_status = "good"