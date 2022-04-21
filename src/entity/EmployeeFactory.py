"""
EmployeeFactory class: A factory that generates Employees objects or Manager objects
Can be used to add more employee types (like IT, marketing, etc.)
#
"""
from typing import Union

from src.entity.Employee import Employee, Manager
from src.entity.EmployeeError import EmployeeTypeError


class EmployeeFactory:  # pizza factory: https://gist.github.com/aadeshnpn/5652878

    @staticmethod
    def create(employee: dict, manager_ids: list[int]) -> Union[Employee, Manager]:  # add type
        try:
            if employee['id'] in manager_ids:
                return Manager(employee_id=employee['id'], first_name=employee['first_name'],
                               manager=employee['manager'], salary=employee['salary'])
            else:
                return Employee(employee_id=employee['id'], first_name=employee['first_name'],
                                manager=employee['manager'], salary=employee['salary'])
        except TypeError as e:
            raise EmployeeTypeError(f'No such Employee type: {e}')
        except Exception as e:
            raise EmployeeTypeError(f'Unknown exception: {e}')
