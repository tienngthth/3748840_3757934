class Util:
    
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()