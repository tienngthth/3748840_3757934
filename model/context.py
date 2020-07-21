import datetime
import os
from .database import Database
from .senseHat import PiSenseHat

class Context:
    temp = None
    humidity = None
    
    @staticmethod
    def update_context():
        raw_data = PiSenseHat.get_data()
        Context.time = datetime.datetime.now().replace(microsecond=0)
        Context.temp = round(Context.get_temp(raw_data), 2)
        Context.humidity = round(raw_data[2], 2)
    
    @staticmethod
    def get_temp(raw_data):
        cpu_temp = Context.get_cpu_temp()
        temp = (raw_data[0] + raw_data[1]) / 2
        return Context.get_smooth(temp - ((cpu_temp - temp) / 1.5))

    @staticmethod
    def get_cpu_temp():
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    # Use moving average to smooth readings.
    @staticmethod
    def get_smooth(x):
        
    @staticmethod
    def log_data_to_db(tb_name, values):
        parameters = (Context.time, Context.temp, Context.humidity)
        Database.insert_record(tb_name, values, parameters)

        if not hasattr(Context.get_smooth, "t"):
            Context.get_smooth.t = [x,x,x]
        
        Context.get_smooth.t[2] = Context.get_smooth.t[1]
        Context.get_smooth.t[1] = Context.get_smooth.t[0]
        Context.get_smooth.t[0] = x

        return (Context.get_smooth.t[0] + Context.get_smooth.t[1] + Context.get_smooth.t[2]) / 3
