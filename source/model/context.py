import datetime
import os
import sys
from .database import Database
from .senseHat import PiSenseHat
from .pushBullet import PushBullet
from .util import Util

"""
Context Class is to create instances of current context and to record them to the database.
Context Class use to get and record sensor data at specific point in time 
"""

class Context:

    #Initialize instance
    def __init__(self):
        self.__timestamp = None
        self.__temp = None
        self.__humidity = None
        self.__temp_status = None
        self.__humidity_status = None
    
    #Update record from user input
    def update_context(self, temperature, humidity, timestamp = None, insert_to_db = False):
        if timestamp is None:
            timestamp = datetime.datetime.now().replace(microsecond=0)
        self.__timestamp = timestamp
        self.__temp = temperature
        self.__humidity = humidity
        if insert_to_db:
            self.__log_data_to_db()

    #Update record from sensor data
    def update_real_time_context(self, insert_to_db = True):
        #Calibration sensor data
        for i in range(3):
            raw_data = PiSenseHat.get_context()
            humidity = Context.get_smooth(raw_data[2])
            temp = Context.get_smooth(self.__correct_temp(raw_data))
        self.__humidity = round(humidity, 2)
        self.__temp = round(temp, 2)
        self.__timestamp = datetime.datetime.now().replace(microsecond=0)
        #Record data to database
        if insert_to_db:
            self.__log_data_to_db()

    #Calibrate temperature sensor data
    def __correct_temp(self, raw_data):
        cpu_temp = self.__get_cpu_temp()
        temp = (raw_data[0] + raw_data[1]) / 2
        return temp - ((cpu_temp - temp) / 1.5)

    #Get CPU temperature
    def __get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    @staticmethod
    # Use moving average to smooth readings.
    def get_smooth(x):
        if not hasattr(Context.get_smooth, "t"):
            Context.get_smooth.t = [x, x ,x]
        
        Context.get_smooth.t[2] = Context.get_smooth.t[1]
        Context.get_smooth.t[1] = Context.get_smooth.t[0]
        Context.get_smooth.t[0] = x

        return (Context.get_smooth.t[0] + Context.get_smooth.t[1] + Context.get_smooth.t[2]) / 3

    #Login to the database
    def __log_data_to_db(self):
        try:
            if Util.check_float(str(self.__temp)) and Util.check_float(str(self.__humidity)):
                parameters = (self.__timestamp, self.__temp, self.__humidity)
                Database.insert_record("((?), (?), (?))", parameters)
            else:
                PushBullet.raise_error("Fail to log data to database, invalid temperature or humidity")
        except:
            PushBullet.raise_error("Fail to log data to database, please check your database and table")

    #Get current context in string
    def get_context_report_record(self):        
        return self.__get_overall_status() + "\n" + self.get_context_message() + "\n"

    #Get current context to write to report
    def __get_overall_status(self):
        if self.temp_status != "good" or self.humidity_status != "good":
            return str(self.__timestamp) + ", BAD"
        else:
            return str(self.__timestamp) + ", OK"

    def get_context_message(self):
        return self.__get_temp_message() + "\n" + self.__get_humidity_message()
    
    #Modify status according to the sensor for appropriate message
    def __get_temp_message(self):
        if (self.temp_status != "good"):
            if (self.temp_status.find("too") != -1):
                return "Temperature is dangerously {}: {} Celsius, BAD".format(self.temp_status, self.__temp)
            else:
                return "Temperature is uncomfortably {}: {} Celsius, BAD".format(self.temp_status, self.__temp)
        else:
            return self.to_string_temp() + ", OK"

    def __get_humidity_message(self):
        if (self.humidity_status != "good"):
            if (self.humidity_status.find("too") != -1):
                return "Humidity is dangerously {}: {} %, BAD".format(self.humidity_status, self.__humidity)
            else:
                return "Humidity is uncomfortably {}: {} %, BAD".format(self.humidity_status, self.__humidity)
        else:
            return self.to_string_humidity() + ", OK"


    #Data getter and setter
    def to_string_humidity(self):
        return "Humidity: {} %".format(self.__humidity)

    def to_string_temp(self):
        return "Temperature: {} Celsius".format(self.__temp)

    @property
    def temp_status(self):
        return self.__temp_status

    @temp_status.setter
    def temp_status(self, temp_status):
        self.__temp_status = temp_status

    @property
    def humidity_status(self):
        return self.__humidity_status

    @humidity_status.setter
    def humidity_status(self, humidity_status):
        self.__humidity_status = humidity_status

    @property
    def humidity(self):
        return self.__humidity

    @property
    def temp(self):
        return self.__temp
