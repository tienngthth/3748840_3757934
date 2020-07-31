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
        print(message + ". Please input letter only, no spaces or special characters")
        file_name = Util.promt_message()
        if file_name == None:
            file_name = default_name
        else:
            while not File.check_file_name(file_name):
                file_name = Util.promt_message()
                if file_name == None:
                    file_name = default_name
                    break
        return file_name + extension

    @staticmethod
    def get_name(default_name, message):
        print(message)
        name = Util.promt_message()
        if name == None:
            return default_name
        else:
            return name

    @staticmethod
    def promt_message():
        print("Please provide input in 5 seconds! Hit Ctrl + C to start")
        try:
            Util.wait_for_start()
        except KeyboardInterrupt:
            name = Util.get_input()
            return name

    @staticmethod
    def wait_for_start():
        for i in range(5):
            sleep(1) 
        print("No input is given. Name is as default")

    @staticmethod
    def get_input():
        tcflush(sys.stdin, TCIFLUSH)
        return input("Input name: ")
        



   