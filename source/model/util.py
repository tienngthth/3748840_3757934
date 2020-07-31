import sys
from .fileHandle import File

class Util:
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()

    @staticmethod
    def get_file_name(default_name, extension, message):
        print(message)
        file_name = File.get_file_name()
        if file_name == None:
            file_name = default_name
        return file_name + extension

    @staticmethod
    def raise_error(message):
        print(message)
        sys.exit()


   