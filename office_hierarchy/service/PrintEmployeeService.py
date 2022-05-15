"""
PrintEmployeeService class
Imports EmployeeTypeError, Manager, and EmployeeBase
"""

from office_hierarchy.entity.Employee import EmployeeBase, Manager
from office_hierarchy.entity.EmployeeError import EmployeeTypeError


class PrintEmployeeService:
    """
    PrintEmployeeService is a service for Employees
    """

    def _set_team_members(self, lookup_employee_dict: dict) -> None:
        """
        Set team_member for Manager
        Sort team_member by first name

        :param lookup_employee_dict: list[dict]
        :return: None
        """
        # Set Manager team_members
        for employee_id, employee in lookup_employee_dict.items():
            if isinstance(employee, Manager):
                # Set team members for manager
                employee.team_members = [em for em in lookup_employee_dict.values() if em.manager == employee_id]
                # Sort team members by first name
                employee.team_members.sort(key=lambda em: em.first_name, reverse=False)

    def _print_hierarchy(self, employee: EmployeeBase, level: int) -> None:
        """
        Recursive method: prints manager and team members.
        Iterates through team_member array and will call itself recursively to add 1 to level for indentation

        :param employee: EmployeeBase object (can be either Employee or Manager objects)
        :param level: int (used as indentation markers)
        :return: None
        """
        print('{}{}'.format(level * '\t', employee.first_name))
        if isinstance(employee, Manager):
            print('{}{} is the manager of:'.format(level * '\t', employee.first_name))
            for team_member in employee.team_members:
                self._print_hierarchy(team_member, level + 1)

    def _print_salary(self, lookup_employee_dict: dict) -> None:
        """
        Print total salary
        :return: None
        """
        total_salary = sum(employee.salary for employee in lookup_employee_dict.values())
        print(f"Total salary: {format(total_salary, ',')}")

    def execute(self, lookup_employee_dict: dict) -> bool:
        """
        Controls the main flow of EmployeeService:
        Sets employee hierarchy with dataset from FileReaderService
        Finds top_managers
        Prints hierarchy
        Print salary

        :return: bool
        :except: EmployeeTypeError, Exception
        """
        try:
            self._set_team_members(lookup_employee_dict)
            # find top managers
            top_managers = [tm for tm in lookup_employee_dict.values() if tm.manager is None]
            if top_managers:
                for top_manager in top_managers:
                    self._print_hierarchy(employee=top_manager, level=0)
                self._print_salary(lookup_employee_dict)
                return True
            else:
                raise EmployeeTypeError('No top manager found')
        except EmployeeTypeError as e:
            print(f'[App {__name__}] EmployeeTypeError: {e}')
        return False
