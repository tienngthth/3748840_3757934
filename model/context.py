import datetime
import os
from .database import Database
from .senseHat import PiSenseHat

class Context:
    timestamp = None
    temp = None
    humidity = None
    temp_status = "good"
    humidity_status = "good"
    
    @staticmethod
    def update_context():
        Context.timestamp = datetime.datetime.now().replace(microsecond=0) 
        for count in [1, 3]:
            raw_data = PiSenseHat.get_data()
            humidity = Context.get_smooth(round(raw_data[2], 2))
            temperature = Context.get_smooth(Context.get_temp(raw_data))
        Context.temp = temperature
        Context.humidity = humidity

    @staticmethod
    def get_temp(raw_data):
        cpu_temp = Context.get_cpu_temp()
        temp = (raw_data[0] + raw_data[1]) / 2
        return temp - ((cpu_temp - temp) / 1.5)

    @staticmethod
    def get_cpu_temp():
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    # Use moving average to smooth readings.
    @staticmethod
    def get_smooth(data):
        if not hasattr(Context.get_smooth, "variable"):
            Context.get_smooth.t = [data,data,data]
        
        Context.get_smooth.variable[2] = Context.get_smooth.variable[1]
        Context.get_smooth.variable[1] = Context.get_smooth.variable[0] 
        Context.get_smooth.variable[0] = data

        return (Context.get_smooth.variable[0] 
                + Context.get_smooth.variable[1] 
                + Context.get_smooth.variable[2]) / 3

    @staticmethod
    def log_data_to_db(tb_name, values):
        parameters = (Context.time, Context.temp, Context.humidity)
        Database.insert_record(tb_name, values, parameters)

    @staticmethod
    def get_context_report_record():
        return str(Context.timestamp) + ":\n" + Context.get_context_message() + "\n"

    @staticmethod
    def get_context_message():
        return Context.get_temp_message + "\n" + Context.get_humidity_message()
    
    @staticmethod
    def get_temp_message():
        if (Context.temp_status != "good"):
            if (Context.temp_status.find("too")):
                return "Temperature is dangerously {}: {} celcius".format(Context.temp_status, Context.temp)
            else:
                return "Temperature is uncomfortably {}: {} celcius".format(Context.temp_status, Context.temp)
        else:
            return Context.to_string_temp()

    @staticmethod
    def get_humidity_message():
        if (Context.humidity_status != "good"):
            if (Context.humidity_status.find("too")):
                return "Humidity is dangerously {}: {} %".format(Context.humidity_status, Context.humidity)
            else:
                return "Humidity is uncomfortably {}: {} %".format(Context.humidity_status, Context.temp)
        else:
            return Context.to_string_humidity()

    @staticmethod
    def to_string_humidity():
        return "Humidity: {} %".format(Context.humidity_status)

    @staticmethod
    def to_string_temp():
        return "Temperature: {} celcius".format(Context.temp)