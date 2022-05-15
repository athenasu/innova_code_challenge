"""
FileUtil class: loads files and returns an array of objects
Can add other file reader methods here if needed
"""

import json
from office_hierarchy.entity.EmployeeError import EmployeeIOError


class FileUtil:

    @staticmethod
    def load_employees_from_json(file_path: str) -> list[dict]:
        """
        Load json file and appends every record into an array

        :param file_path:str
        :return: list[dict]
        :raises: EmployeeIOError(FileNotFound), EmployeeIOError(JSONDecoderError)
        """
        try:
            with open(file_path) as f:
                json_list = json.load(f)
                records = []
                for obj in json_list:
                    records.append(obj)
            return records
        except json.JSONDecodeError as e:
            raise EmployeeIOError(f'[Util {__name__}] Wrong json format: {e}')

