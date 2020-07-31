import json
import pathlib
import sys

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
    def check_file_name(name):
        if not name.isalpha():
            print("Invalid name")
            return False
        else:
            return True

