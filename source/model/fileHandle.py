import json
import pathlib
import sys
from termios import tcflush, TCIFLUSH
from time import sleep

class File:

    @staticmethod
    def read_json(file_name):
        json_file = open(pathlib.Path(__file__).parent.parent / "files" / file_name)
        json_content = json.load(json_file)
        json_file.close
        return json_content

    @staticmethod
    def write_json(file_name, json_content):
        json_file = open(pathlib.Path(__file__).parent.parent / "files" /  file_name, "w")
        json_file.write(json.dumps(json_content))
        json_file.close()

    @staticmethod
    def write_csv(file_name, file_content):
        csv_file = open(pathlib.Path(__file__).parent.parent / "files" /  file_name, "a")
        csv_file.write(file_content)
        csv_file.close()

    @staticmethod
    def get_file_name():
        print("Please provide input in 10 seconds! Hit Ctrl + C to start")
        try:
            File.wait_for_start()
        except KeyboardInterrupt:
            name = File.get_name()
            while not File.check_file_name(name):
                name = File.get_name()
            return name

    @staticmethod
    def wait_for_start():
        for i in range(0,5):
            sleep(1) 
        print("No input is given. File name is as default")

    @staticmethod
    def get_name():
        tcflush(sys.stdin, TCIFLUSH)
        return input("Input file name (letter only, no spaces or special characters): ")
        
    @staticmethod
    def check_file_name(name):
        if not name.isalpha():
            print("Invalid name")
            return False
        else:
            return True


