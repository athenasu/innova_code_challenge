"""
EmployeeService class
Imports lru_cache, EmployeeFactory, Manager, and EmployeeBase
Benchmark EmployeeServiceMock for non-recursive method
"""
from functools import lru_cache
from util.FileUtil import FileUtil
from src.entity.EmployeeFactory import EmployeeFactory
from src.entity.Employee import Manager, EmployeeBase
from src.entity.EmployeeError import EmployeeIOError, EmployeeTypeError


class EmployeeService:  # description of class

    def __init__(self):
        self.hierarchy_dict: dict[int, int] = {}
        self.lookup_employee_dict: dict[int, EmployeeBase] = {}

    @lru_cache(maxsize=100)
    def set_employee_level(self, employee_id: int, employee_level: int) -> int:
        """
        Recursive method that sets employee levels by using emp_id and emp_level
        Hierarchy starts from top manager, level starts at 0
        Performance: (pytest/timeit benchmark)

        :param employee_id: int
        :param employee_level: int
        """
        current_employee_obj = self.lookup_employee_dict[employee_id]
        if current_employee_obj is None or current_employee_obj.manager is None:
            return employee_level

        next_employee_obj = self.lookup_employee_dict[current_employee_obj.manager]
        return self.set_employee_level(next_employee_obj.employee_id, employee_level + 1)

    def set_employee_hierarchy(self, employees: list[dict]) -> None:
        """
        Sets hierarcy_dict to group manager_ids with team_member ids
        Creates Manager and Employee objects
        Calls set_employee_level() and sets levels for all employees

        :param employees: list[dict]
        :return: None
        """
        # Set hierarchy_dict
        for employee in employees:
            self.hierarchy_dict[employee['manager']] = employee['id']

        # Create Manager and Employee objects
        manager_ids = list(self.hierarchy_dict.keys())
        for employee in employees:
            self.lookup_employee_dict[employee['id']] = EmployeeFactory.create(employee=employee, manager_ids=manager_ids)

        # Set employee level (recursive) and set manager's team members
        for employee_id, employee in self.lookup_employee_dict.items():
            employee.level = self.set_employee_level(employee_id, 0)
            if employee_id in manager_ids:
                # Set team members for manager
                employee.team_members = [emp for emp in self.lookup_employee_dict.values() if emp.manager == employee_id]

    def print_hierarchy(self) -> None:
        """
        Get managers
        Sort manager levels
        Print manager and their team members

        :return: None
        """
        # Get Managers
        managers = [employee for employee in self.lookup_employee_dict.values() if isinstance(employee, Manager)]
        # Sort manager.levels from 0
        managers.sort(key=lambda x: x.level, reverse=False)
        # Print manager team members
        for manager in managers:
            print('{} {} is the manager of:'.format(manager.level * '\t', manager.first_name))
            # Sort team_members by first_name
            manager.team_members.sort(key=lambda x: x.first_name, reverse=False)
            for team_member in manager.team_members:
                print('{} {}'.format(team_member.level * '\t', team_member.first_name))

    def set_total_salary(self, employees: dict[int, EmployeeBase]) -> int:
        """
        Return sum of employee salary

        :param employees: dict[int, EmployeeBase]
        :return: int
        """
        if not employees:
            return 0
        return sum(employee.salary for employee in employees.values())

    def execute(self, json_filename: str) -> None:  # handle all error handling (top level function)
        """
        Calls functions in EmployeeService to print office hierarchy

        :param json_filename: str
        :return: None
        """
        try:
            employees = FileUtil.load_employees_from_json(json_filename=json_filename)
            self.set_employee_hierarchy(employees)
            self.print_hierarchy()
            print(f"Total salary: {format(self.set_total_salary(self.lookup_employee_dict), ',')}")
        except EmployeeIOError as e:
            print(f'[App {__name__}] IOError: {e}')
        except EmployeeTypeError as e:
            print(f'[App {__name__}] TypeError: {e}')
        except Exception as e:
            print(f'[App {__name__}] Unknown exception: {e}')
