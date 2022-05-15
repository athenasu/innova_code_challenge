"""
EmployeeFactory class: A factory that generates Employees objects or Manager objects
Can be used to add more employee types (like IT, marketing, etc.)
"""
from typing import Union

from office_hierarchy.entity.Employee import Employee, Manager
from office_hierarchy.entity.EmployeeError import EmployeeTypeError
from office_hierarchy.service.FileReaderService import FileReaderService


class EmployeeFactory:
    """
    EmployeeFactory class: A factory that generates Employees objects or Manager objects
    """
    file_reader_service = FileReaderService()

    @staticmethod
    def create(file_path: str) -> dict[int, Union[Manager, Employee]]:
        """
        Calls FileReaderService and gets a dataset
        Creates and appends Employee or Manager objects

        :return: dictionary of Manager and Employee objects
        :raises: EmployeeTypeError(TypeError), EmployeeTypeError(Exception)
        """
        # Get dataset from FileReaderService
        employees = EmployeeFactory.file_reader_service.collect_json_file(file_path=file_path)
        # Set manager_ids in EmployeeFactory
        manager_ids = {emp['manager'] for emp in employees}
        lookup_employee_dict = {}
        for employee in employees:
            try:
                employee_id: int = employee.get('id')
                if employee_id in manager_ids:
                    lookup_employee_dict[employee_id] = Manager(employee_id=employee_id,
                                                                first_name=employee['first_name'],
                                                                manager=employee['manager'], salary=employee['salary'])
                else:
                    lookup_employee_dict[employee_id] = Employee(employee_id=employee_id,
                                                                 first_name=employee['first_name'],
                                                                 manager=employee['manager'], salary=employee['salary'])
            except Exception as e:
                raise EmployeeTypeError(f'EmployeeFactory- {type(e).__name__}: {e}')
        return lookup_employee_dict
