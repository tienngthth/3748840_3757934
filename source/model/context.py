import datetime
import os
from .database import Database
from .senseHat import PiSenseHat

class Context:
    timestamp = None
    temp = None
    humidity = None
    temp_status = None
    humidity_status = None
    
    @staticmethod
    def update_context(timestamp = None, temperature = None, humidity = None):
        if humidity == None or temperature == None or timestamp == None:
            Context.update_real_time()
        else:
            Context.temp = temperature
            Context.humidity = humidity
            Context.timestamp = timestamp

    @staticmethod
    def update_real_time():
        raw_data = PiSenseHat.get_context()
        Context.humidity = round(raw_data[2], 2)
        Context.temp = round(Context.correct_temp(raw_data), 2)

    def set_context(context):
        Context.time = datetime.datetime.now().replace(microsecond=0)
        Context.temp = round(context[0], 2)
        Context.humidity = round(context[1], 2)
    
    @staticmethod
    def log_data_to_db(tb_name, values):
        parameters = (Context.time, Context.temp, Context.humidity)
        Database.insert_record(tb_name, values, parameters)
        Context.timestamp = datetime.datetime.now().replace(microsecond=0) 

    @staticmethod
    def correct_temp(raw_data):
        cpu_temp = Context.get_cpu_temp()
        temp = (raw_data[0] + raw_data[1]) / 2
        return temp - ((cpu_temp - temp) / 1.5)

    @staticmethod
    def get_cpu_temp():
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    @staticmethod
    def log_data_to_db():
        parameters = (Context.timestamp, Context.temp, Context.humidity)
        Database.insert_record("((?), (?), (?))", parameters)

    @staticmethod
    def get_context_report_record():        
        return Context.get_overall_status() + "\n" + Context.get_context_message() + "\n"

    @staticmethod
    def get_overall_status():
        if Context.temp_status != "good" or Context.humidity_status != "good":
            return str(Context.timestamp) + ", BAD"
        else:
            return str(Context.timestamp) + ", OK"

    @staticmethod
    def get_context_message():
        return Context.get_temp_message() + "\n" + Context.get_humidity_message()
    
    @staticmethod
    def get_temp_message():
        if (Context.temp_status != "good"):
            if (Context.temp_status.find("too") != -1):
                return "Temperature is dangerously {}: {} Celsius, BAD".format(Context.temp_status, Context.temp)
            else:
                return "Temperature is uncomfortably {}: {} Celsius, BAD".format(Context.temp_status, Context.temp)
        else:
            return Context.to_string_temp() + ", OK"

    @staticmethod
    def get_humidity_message():
        if (Context.humidity_status != "good"):
            if (Context.humidity_status.find("too") != -1):
                return "Humidity is dangerously {}: {} %, BAD".format(Context.humidity_status, Context.humidity)
            else:
                return "Humidity is uncomfortably {}: {} %, BAD".format(Context.humidity_status, Context.humidity)
        else:
            return Context.to_string_humidity() + ", OK"

    @staticmethod
    def to_string_humidity():
        return "Humidity: {} %".format(Context.humidity)

    @staticmethod
    def to_string_temp():
        return "Temperature: {} Celsius".format(Context.temp)

