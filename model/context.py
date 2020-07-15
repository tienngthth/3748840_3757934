import datetime

class Context:
    temp = None
    humidity = None
    
    @staticmethod
    def set_context(context):
        Context.time = datetime.datetime.now().strftime("%X")
        Context.temp = round(context[0], 2)
        Context.humidity = round(context[1], 2)