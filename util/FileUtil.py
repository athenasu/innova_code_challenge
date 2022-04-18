"""
FileUtil class: loads json files from resource folder and returns an array of objects
"""

import json
from src.entity.EmployeeError import EmployeeIOError


class FileUtil:

    @staticmethod
    def load_employees_from_json(json_filename: str) -> list[dict]:
        """
        Load json file and appends every record into an array

        :param json_filename:str
        :return: list[dict]
        """
        try:
            with open(f'../resources/{json_filename}', 'r') as f:
                json_list = json.load(f)
                records = []
                for obj in json_list:
                    records.append(obj)
            if len(records) == 0:
                raise TypeError('File cannot be empty')
            else:
                return records
        except FileNotFoundError as e:
            raise EmployeeIOError(f'[Util {__name__}] File not found: {e}')
        except json.JSONDecodeError as e:
            raise EmployeeIOError(f'[Util {__name__}] Wrong json format: {e}')
        except TypeError as e:
            raise EmployeeIOError(f'[Util {__name__}] File cannot be empty: {e}')
        except Exception as e:
            raise EmployeeIOError(f'[Util {__name__}] Unknown exception: {e}')

    def load_employee_from_xml(self):
        pass
