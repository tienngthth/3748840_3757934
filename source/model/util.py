class Util:
    
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()

    @staticmethod
    def get_file_name(default):
        file_name = File.get_file_name()
        if file_name == None:
            file_name = default
        return file_name + ".csv"