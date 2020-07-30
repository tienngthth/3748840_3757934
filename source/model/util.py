from .fileHandle import File

class Util:
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()

    @staticmethod
    def get_csv_file_name(default_name):
        return Util.get_file_name(default_name) + ".csv"

    @staticmethod
    def get_json_file_name(default_name):
        return Util.get_file_name(default_name) + ".json"

    @staticmethod
    def get_file_name(default_name):
        file_name = File.get_file_name()
        if file_name == None:
            file_name = default_name
        return file_name

   