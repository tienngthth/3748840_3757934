class Preference:
    cold_max = None
    comfortable_min = None
    comfortable_max = None
    hot_min = None
    comfortable_status = None
    create_new_table = None

    @staticmethod
    def set_preference(
        cold_max, comfortable_min, 
        comfortable_max, hot_min, 
        comfortable_status, create_new_table
    ):
        Preference.set_cold_max(cold_max)
        Preference.set_comfortable_min(comfortable_min)
        Preference.set_comfortable_max(comfortable_max)
        Preference.set_hot_min(hot_min)
        Preference.set_comfortable_status(comfortable_status)
        Preference.set_create_new_table(create_new_table)
    
    @staticmethod
    def set_cold_max(cold_max):
        Preference.cold_max = cold_max

    @staticmethod
    def set_comfortable_min(comfortable_min):
        Preference.comfortable_min = comfortable_min
    
    @staticmethod
    def set_comfortable_max(comfortable_max):
        Preference.comfortable_max = comfortable_max

    @staticmethod
    def set_hot_min(hot_min):
        Preference.hot_min = hot_min
    
    @staticmethod
    def set_comfortable_status(comfortable_status):
        Preference.comfortable_status = comfortable_status

    @staticmethod
    def set_create_new_table(create_new_table):
        Preference.create_new_table = create_new_table

    @staticmethod
    def check_comfortable(temp):
        if temp > Preference.comfortable_max:
            return "hot"
        elif temp < Preference.comfortable_min:
            return "cold"
        else:
            return "good"