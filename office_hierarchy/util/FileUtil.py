"""
FileUtil class: loads files and returns an array of objects
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
        """
        try:
            with open(file_path) as f:
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
