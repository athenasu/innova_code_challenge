"""
PrintEmployeeService class
Imports lru_cache, EmployeeFactory, Manager, and EmployeeBase
"""
from functools import lru_cache

from office_hierarchy.entity.Employee import EmployeeBase, Manager
from office_hierarchy.entity.EmployeeError import EmployeeIOError, EmployeeTypeError
from office_hierarchy.entity.EmployeeFactory import EmployeeFactory
from office_hierarchy.util.FileUtil import FileUtil


class PrintEmployeeService:
    """
    PrintEmployeeService is a service for Employees
    """

    def __init__(self):
        self.lookup_employee_dict: dict[int, EmployeeBase] = {}

    @lru_cache(maxsize=100)
    def _set_employee_level(self, employee_id: int, employee_level: int = 0) -> int:
        """
        Recursive method that sets employee levels by using emp_id and emp_level
        Hierarchy starts from top manager, level starts at 0

        :param employee_id: int
        :param employee_level: int
        :return: int
        """
        current_employee_obj = self.lookup_employee_dict[employee_id]
        if current_employee_obj is None or current_employee_obj.manager is None:
            return employee_level

        manager_employee_obj = self.lookup_employee_dict[current_employee_obj.manager]
        return self._set_employee_level(manager_employee_obj.employee_id, employee_level + 1)

    def _set_employee_hierarchy(self, employees: list[dict]) -> None:
        """
        Set manager_ids
        Create Manager and Employee objects
        Call set_employee_level() and sets levels for all employees
        Set team_member for Manager

        :param employees: list[dict]
        :return: None
        """
        # Create manager_ids set
        manager_ids = set(map(lambda emp: emp["manager"], employees))
        # Create Manager and Employee objects
        for employee in employees:
            self.lookup_employee_dict[employee['id']] = EmployeeFactory.create(employee=employee, manager_ids=manager_ids)

        # Set employee level (recursive) and set manager's team members
        for employee_id, employee in self.lookup_employee_dict.items():
            employee.level = self._set_employee_level(employee_id)
            if isinstance(employee, Manager):
                # Set team members for manager
                employee.team_members = [emp for emp in self.lookup_employee_dict.values() if emp.manager == employee_id]

    def _print_hierarchy(self) -> None:
        """
        Get managers
        Sort manager levels
        Print manager and their team members

        :return: None
        """
        # Get Managers
        managers = [employee for employee in self.lookup_employee_dict.values() if isinstance(employee, Manager)]
        # Sort manager.levels from 0
        managers.sort(key=lambda mgr: mgr.level, reverse=False)
        # Print manager team members
        for manager in managers:
            print('{}{} is the manager of:'.format(manager.level * '\t', manager.first_name))
            # Sort team_members by first_name
            manager.team_members.sort(key=lambda emp: emp.first_name, reverse=False)
            for team_member in manager.team_members:
                print('{}{}'.format(team_member.level * '\t', team_member.first_name))
        total_salary = sum(employee.salary for employee in self.lookup_employee_dict.values())
        print(f"Total salary: {format(total_salary, ',')}")

    def execute(self, file_path: str) -> bool:
        """
        Controls the main flow of EmployeeService:
        Gets employee dictionary from FileUtil.load_employees_from_json
        Sets employee hierarchy
        Prints office hierarchy
        Prints total salary

        :param file_path: str
        :return: bool
        """
        try:
            employees = FileUtil.load_employees_from_json(file_path=file_path)
            self._set_employee_hierarchy(employees)
            self._print_hierarchy()

            return True
        except EmployeeIOError as e:
            print(f'[App {__name__}] IOError: {e}')
        except EmployeeTypeError as e:
            print(f'[App {__name__}] TypeError: {e}')
        except Exception as e:
            print(f'[App {__name__}] Unknown exception: {e}')

        return False
