import json
import pathlib

class File:

    @staticmethod
    def read_json(file_name):
        config_file = open(pathlib.Path(__file__).parent.parent / "files" / file_name)
        json_content = json.load(config_file)
        config_file.close
        return json_content

    @staticmethod
    def write_json(file_name, json_content):
        status_file = open(pathlib.Path(__file__).parent.parent / "files" /  file_name, "w")
        status_file.write(json.dumps(json_content))
        status_file.close()
