import json
import pathlib
import sys

"""
Class File is used to handle all the file manipulation required in assignment 1
"""
class File:

    #Retrive json file to json object in python
    @staticmethod
    def read_json(file_name):
        json_file = open(pathlib.Path(__file__).parent.parent / "files" / file_name)
        json_content = json.load(json_file)
        json_file.close
        return json_content

    #Modify the json content of a json file
    @staticmethod
    def write_json(file_name, json_content):
        json_file = open(pathlib.Path(__file__).parent.parent / "files" /  file_name, "w")
        json_file.write(json.dumps(json_content))
        json_file.close()

    #Modify the csv content of a csv file
    @staticmethod
    def write_csv(file_name, file_content):
        csv_file = open(pathlib.Path(__file__).parent.parent / "files" /  file_name, "a")
        csv_file.write(file_content)
        csv_file.close()

    #Check user input a valid file name (only contain the alphabetical characters)
    @staticmethod
    def check_file_name(name):
        if not name.isalpha():
            print("Invalid name")
            return False
        else:
            return True

