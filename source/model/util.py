import sys
from termios import tcflush, TCIFLUSH
from time import sleep
from .fileHandle import File

class Util:
    @staticmethod
    def check_float(float_string):
        if float_string.find(".") != -1:
            return float_string.replace('.', '', 1).isdigit()
        else:
            return float_string.isdigit()

    @staticmethod
    def raise_error(message):
        print(message)
        sys.exit()

    @staticmethod
    def get_file_name(default_name, extension, message):
        print(message)
        file_name = Util.get_input("Please input letter only, no spaces or special characters")
        if file_name != default_name:
            while not File.check_file_name(file_name):
                file_name = Util.get_input("Please input letter only, no spaces or special characters")
                if file_name == default_name:
                    break
        return file_name + extension

    @staticmethod
    def get_input(default_input, message):
        print(message)
        user_input = Util.promt_message()
        if user_input == None:
            return default_input
        else:
            return user_input

    @staticmethod
    def promt_message():
        print("Please provide input in 5 seconds! Hit Ctrl + C to start")
        try:
            Util.wait_for_start()
        except KeyboardInterrupt:
            user_input = Util.get_input()
            return user_input

    @staticmethod
    def wait_for_start():
        for i in range(5):
            sleep(1) 
        print("No input is given. Name is as default")

    @staticmethod
    def get_input():
        tcflush(sys.stdin, TCIFLUSH)
        return input("Input name: ")
        



   