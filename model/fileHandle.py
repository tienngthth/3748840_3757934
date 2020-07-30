import json
import sys
import pathlib
from time import sleep
from termios import tcflush, TCIFLUSH

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
        print('Please provide input in 20 seconds! Hit Ctrl + C to start')
        try:
            for i in range(0,5):
                sleep(1) 
            print('No input is given. File name is as default')
        except KeyboardInterrupt:
            tcflush(sys.stdin, TCIFLUSH)
            return input('Input file name: ')
