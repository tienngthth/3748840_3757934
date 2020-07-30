import datetime
import os
import sys
from .database import Database
from .senseHat import PiSenseHat

class Context:
    def __init__(self):
        self.__timestamp = None
        self.__temp = None
        self.__humidity = None
        self.__temp_status = None
        self.__humidity_status = None
    
    def update_context(self, temperature, humidity, timestamp = None, insert_to_db = False):
        if timestamp is None:
            timestamp = datetime.datetime.now().replace(microsecond=0)
        self.timestamp = timestamp
        self.temp = temperature
        self.humidity = humidity
        if insert_to_db:
            self.__log_data_to_db()

    def update_real_time_context(self, insert_to_db = True):
        raw_data = PiSenseHat.get_context()
        self.humidity = round(raw_data[2], 2)
        self.temp = round(self.__correct_temp(raw_data), 2)
        self.time = datetime.datetime.now().replace(microsecond=0)
        if insert_to_db:
           self.__log_data_to_db()

    def __correct_temp(self, raw_data):
        cpu_temp = self.__get_cpu_temp()
        temp = (raw_data[0] + raw_data[1]) / 2
        return temp - ((cpu_temp - temp) / 1.5)

    def __get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    def __log_data_to_db(self):
        try:
            parameters = (self.timestamp, self.temp, self.humidity)
            Database.insert_record("((?), (?), (?))", parameters)
        except:
            print("Unable to log data to database")
            sys.exit()

    def get_context_report_record(self):        
        return self.__get_overall_status() + "\n" + self.get_context_message() + "\n"

    def __get_overall_status(self):
        if self.temp_status != "good" or self.humidity_status != "good":
            return str(self.timestamp) + ", BAD"
        else:
            return str(self.timestamp) + ", OK"

    def get_context_message(self):
        return self.__get_temp_message() + "\n" + self.__get_humidity_message()
    
    def __get_temp_message(self):
        if (self.temp_status != "good"):
            if (self.temp_status.find("too") != -1):
                return "Temperature is dangerously {}: {} Celsius, BAD".format(self.temp_status, self.temp)
            else:
                return "Temperature is uncomfortably {}: {} Celsius, BAD".format(self.temp_status, self.temp)
        else:
            return self.to_string_temp() + ", OK"

    def __get_humidity_message(self):
        if (self.humidity_status != "good"):
            if (self.humidity_status.find("too") != -1):
                return "Humidity is dangerously {}: {} %, BAD".format(self.humidity_status, self.humidity)
            else:
                return "Humidity is uncomfortably {}: {} %, BAD".format(self.humidity_status, self.humidity)
        else:
            return self.to_string_humidity() + ", OK"

    def to_string_humidity(self):
        return "Humidity: {} %".format(self.humidity)

    def to_string_temp(self):
        return "Temperature: {} Celsius".format(self.temp)

    @property
    def temp_status(self):
        return self.__temp_status

    @property
    def humidity_status(self):
        return self.__humidity_status
