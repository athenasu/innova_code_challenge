import importlib.resources
import json


class FileUtil:

    @staticmethod  # public package for everyone to use
    def load_employees_from_json(json_filename: str) -> list[dict]:
        try:
            with importlib.resources.open_text('resources', json_filename) as f:
                json_list = json.load(f)
                records = []
                for obj in json_list:
                    records.append(obj)
            return records
        except FileNotFoundError as e:
            raise FileNotFoundError('File does not exist')
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError('Wrong json format')
        except TypeError:
            raise TypeError('Type unexpected')

    def load_employee_from_xml(self):
        pass
