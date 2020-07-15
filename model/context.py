import datetime

class Context:
    temp = None
    humidity = None
    
    @staticmethod
    def set_context(temp, humidity):
        Context.time = datetime.datetime.now().strftime("%X")
        Context.temp = round(temp, 2)
        Context.humidity = round(humidity, 2)