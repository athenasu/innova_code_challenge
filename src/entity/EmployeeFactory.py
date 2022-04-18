"""
EmployeeFactory class: A factory that generates Employees or Managers
"""

from src.entity.Employee import Manager, Employee
from src.entity.EmployeeError import EmployeeTypeError


class EmployeeFactory:  # pizza factory: https://gist.github.com/aadeshnpn/5652878

    @staticmethod
    def create(employee, manager_ids: list[int]):
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
