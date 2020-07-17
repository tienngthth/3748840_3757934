import datetime
from .database import Database

class Context:
    temp = None
    humidity = None
    
    @staticmethod
    def set_context(context):
        Context.time = datetime.datetime.now().replace(microsecond=0)
        Context.temp = round(context[0], 2)
        Context.humidity = round(context[1], 2)
    
    @staticmethod
    def log_data_to_db(tb_name, values):
        parameters = (Context.time, Context.temp, Context.humidity)
        Database.insert_record(tb_name, values, parameters)
