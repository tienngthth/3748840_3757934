import sys
from .fileHandle import File
from .context import Context
from .util import Util

class Preference:
    def __init__(self, preference_file_name, status_file_name):
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
        self.__preference_file_name = preference_file_name
        self.__status_file_name = status_file_name
        self.read_preference()

    def read_preference(self):
        try:
            preference_json = File.read_json(self.preference_file_name)
            status_json = File.read_json(self.status_file_name)
        except:
            print("Preference or status file is missing or having wrong content format")
            sys.exit()
        self.__parse_json(preference_json, status_json)

    def __parse_json(self, preference_json, status_json):
        self.__validate_preference_values(preference_json)
        self.__validate_status_data(status_json)
        self.__set_preference (
            float(preference_json["cold_max"]),
            float(preference_json["comfortable_min_temp"]),
            float(preference_json["comfortable_max_temp"]),
            float(preference_json["hot_min"]),
            float(preference_json["dry_max"]),
            float(preference_json["comfortable_min_humidity"]),
            float(preference_json["comfortable_max_humidity"]),
            float(preference_json["humid_min"]),
            status_json["comfortable_status"],
            status_json["create_new_table"]
    )

    def __validate_status_values(self, statuses_dict):
        for key, value in values_dict.items():
            if type(value) is not bool:
                print("Wrong " + key + " data type, invalid boolean")
                sys.exit()

    def __validate_preference_values(self, values_dict):
        values = []
        for key, value in values_dict.items():
            if not Util.check_float(str(value)):
                print("Wrong " + key + " data type, invalid number")
                sys.exit()
            else:
                values.append(value)
        self.__check_context_preference_value_order(values[:4])
        self.__check_context_preference_value_order(Values[4:])
        
    def __check_context_preference_value_order(self, values):
        for i in range(0, 3]):
            if values[i] > values[i + 1]:
                print("Invalid context preference values order")
                sys.exit()

    def __set_preference(
        self, 
        cold_max, comfortable_min_temp, 
        comfortable_max_temp, hot_min, 
        dry_max, comfortable_min_humidity, 
        comfortable_max_humidity, humid_min, 
        comfortable_status, create_new_table
    ):
        self.cold_max = cold_max
        self.comfortable_min_temp = comfortable_min_temp
        self.comfortable_max_temp = comfortable_max_temp
        self.hot_min = hot_min
        self.dry_max = dry_max
        self.comfortable_min_humidity = comfortable_min_humidity
        self.comfortable_max_humidity = comfortable_max_humidity
        self.humid_min = humid_min
        self.comfortable_status = comfortable_status
        self.create_new_table = create_new_table

    def check_context(self):
        self.__check_humidity()
        self.__check_temp()

    def __check_humidity(self):
        if Context.humidity > self.humid_min:
            Context.humidity_status = "too humid"
        elif Context.humidity > self.comfortable_max_humidity:
            Context.humidity_status = "humid"
        elif Context.humidity < self.dry_max:
            Context.humidity_status = "too dry"
        elif Context.humidity < self.comfortable_min_humidity:
            Context.humidity_status = "dry"
        else:
            Context.humidity_status = "good"

    def __check_temp(self):
        if Context.temp > self.hot_min:
            Context.temp_status = "too hot"
        elif Context.temp > self.comfortable_max_temp:
            Context.temp_status = "hot"
        elif Context.temp < self.cold_max:
            Context.temp_status = "too cold"
        elif Context.temp < self.comfortable_min_temp:
            Context.temp_status = "cold"
        else:
            Context.temp_status = "good"

      @property
    def timestamp(self):
        return self.__timestamp

    @property
    def comfortable_status(self):
        return self.__comfortable_status

    @comfortable_status.setter
    def comfortable_status(self, comfortable_status):
        self.comfortable_status = comfortable_status

    @property
    def create_new_table(self):
        return self.__create_new_table

    @create_new_table.setter
    def create_new_table(self, create_new_table):
        self.create_new_table = create_new_table

    @property
    def status_file_name(self):
        return self.__status_file_name