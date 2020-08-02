import sys
from termios import tcflush, TCIFLUSH
from time import sleep
from .fileHandle import File

"""
Class Util is use to handle simple function that are used accross all applications.
"""
class Util:

    #Check if the input is a float or not
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()

    #Send error and stop system
    @staticmethod
    def raise_error(message):
        print(message)
        sys.exit()

    #Get file name from user input
    @staticmethod
    def get_file_name(default_name, extension, message):
        print(message)
        file_name = Util.get_user_input(default_name, "Please input letter only, no spaces or special characters")
        if file_name != default_name:
            #Check till the user input a validate input
            while not File.check_file_name(file_name):
                file_name = Util.get_user_input(default_name, "Please input letter only, no spaces or special characters")
                if file_name == default_name:
                    break
        return file_name + extension

    #Get user input
    @staticmethod
    def get_user_input(default_input, message):
        print(message)
        user_input = Util.promt_message()
        if user_input == None:
            return default_input
        else:
            return user_input

    #Promt message
    @staticmethod
    def promt_message():
        print("Please provide input in 5 seconds! Hit Ctrl + C to start")
        try:
            Util.wait_for_start()
        #Start getting input after user press Ctrl + C
        except KeyboardInterrupt:
            user_input = Util.get_input()
            return user_input

    #Wait for user input
    @staticmethod
    def wait_for_start():
        for i in range(5):
            sleep(1) 
        print("No input is given. Name is as default")

    #Get input from CLI
    @staticmethod
    def get_input():
        tcflush(sys.stdin, TCIFLUSH)
        return input("Input name: ")
        



   