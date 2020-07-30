from .fileHandle import File
from .preference import Preference

class Util:
    
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()

    @staticmethod
    def get_csv_file_name(default):
        return File.get_file_name(default) + ".csv"

    @staticmethod
    def get_json_file_name(default):
        return File.get_file_name(default) + ".json"

    @staticmethod
    def get_file_name(default):
        file_name = File.get_file_name()
        if file_name == None:
            file_name = default
        return file_name

    @staticmethod
    def read_preference():
        print("Input preference file name. Default name is config.csv")
        preference_file_name = Util.get_json_file_name("config")
        print("Input preference file name. Default name is status.csv")
        status_file_name = Util.get_json_file_name("status")
        return Preference(preference_file_name, status_file_name)