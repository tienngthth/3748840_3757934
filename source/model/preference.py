import sys
from .fileHandle import File
from .context import Context
from .util import Util
from .pushBullet import PushBullet

"""
"""
class Preference:
    
    #Initialize instance of the preference
    def __init__(self):
        self.__cold_max = None
        self.__comfortable_min_temp = None
        self.__comfortable_max_temp = None
        self.__hot_min = None
        self.__dry_max = None
        self.__comfortable_min_humidity = None
        self.__comfortable_max_humidity = None
        self.__humid_min = None
        self.__comfortable_status = None
        self.__create_new_table = None
        self.__config_file_name = "config.json"
        self.__status_file_name = "status.json"
        self.read_preference()

    #Read preference from json file
    def read_preference(self):
        try:
            config_json = File.read_json(self.__config_file_name)
            status_json = File.read_json(self.__status_file_name)
        except:
            PushBullet.send_notification("Preference or status file is missing or having wrong content format, invalid json format")
            sys.exit()
        self.__parse_json(config_json, status_json)

    #Match json content to preference variables
    def __parse_json(self, config_json, status_json):
        #Validate json content
        self.__validate_config_values(config_json)
        self.__validate_status_values(status_json)
        try:
            self.__set_preference (
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
        except:
            PushBullet.raise_error("Missing required values in config.json or status.json file")

    #Validate status json file 
    def __validate_status_values(self, status_dict):
        if len(status_dict) != 2:
            PushBullet.raise_error("Wrong number of values in status.json")
        #Check if all values are boolean type
        for key, value in status_dict.items():
            if type(value) is not bool:
                PushBullet.raise_error("Wrong " + key + " data type, invalid boolean")

    #Validate config json file     
    def __validate_config_values(self, config_dict):
        values = []
        if len(config_dict) != 8:
            PushBullet.raise_error("Wrong number of values in config.json")
        #Check if all values are in valid format
        for key, value in config_dict.items():
            if not Util.check_float(str(value)):
                PushBullet.raise_error("Wrong " + key + " data type, invalid number")
            else:
                values.append(value)
        self.__check_config_value_order(values[:4])
        self.__check_config_value_order(values[4:])
    
    #Check if all values are in correct order
    def __check_config_value_order(self, values):
        for i in range(3):
            if values[i] > values[i + 1]:
                PushBullet.raise_error("Invalid context preference values order")

    #Match variables with values
    def __set_preference(
        self, 
        cold_max, comfortable_min_temp, 
        comfortable_max_temp, hot_min, 
        dry_max, comfortable_min_humidity, 
        comfortable_max_humidity, humid_min, 
        comfortable_status, create_new_table
    ):
        self.__cold_max = cold_max
        self.__comfortable_min_temp = comfortable_min_temp
        self.__comfortable_max_temp = comfortable_max_temp
        self.__hot_min = hot_min
        self.__dry_max = dry_max
        self.__comfortable_min_humidity = comfortable_min_humidity
        self.__comfortable_max_humidity = comfortable_max_humidity
        self.__humid_min = humid_min
        self.comfortable_status = comfortable_status
        self.create_new_table = create_new_table

    #Check all environmental context
    def check_context(self, context):
        self.__check_humidity(context)
        self.__check_temp(context)

    #Check humidity
    def __check_humidity(self, context):
        if context.humidity > self.__humid_min:
            context.humidity_status = "too humid"
        elif context.humidity > self.__comfortable_max_humidity:
            context.humidity_status = "humid"
        elif context.humidity < self.__dry_max:
            context.humidity_status = "too dry"
        elif context.humidity < self.__comfortable_min_humidity:
            context.humidity_status = "dry"
        else:
            context.humidity_status = "good"

    #Check temperature
    def __check_temp(self, context):
        if context.temp > self.__hot_min:
            context.temp_status = "too hot"
        elif context.temp > self.__comfortable_max_temp:
            context.temp_status = "hot"
        elif context.temp < self.__cold_max:
            context.temp_status = "too cold"
        elif context.temp < self.__comfortable_min_temp:
            context.temp_status = "cold"
        else:
            Context.temp_status = "good"


    #Getters and setters
    @property
    def comfortable_status(self):
        return self.__comfortable_status

    @comfortable_status.setter
    def comfortable_status(self, comfortable_status):
        self.__comfortable_status = comfortable_status

    @property
    def create_new_table(self):
        return self.__create_new_table

    @create_new_table.setter
    def create_new_table(self, create_new_table):
        self.__create_new_table = create_new_table

    @property
    def status_file_name(self):
        return self.__status_file_name