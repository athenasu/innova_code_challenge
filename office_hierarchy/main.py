"""
Main function that calls EmployeeService
"""
from office_hierarchy.entity.EmployeeFactory import EmployeeFactory
from office_hierarchy.service.PrintEmployeeService import PrintEmployeeService


def print_office_hierarchy() -> None:
    """
    Interactive method to choose which files to access
    Calls EmployeeFactory's create() method to get list of dictionaries
    Calls PrintEmployeeService's execute() method to print hierarchy
    :return: None
    """

    while True:
        employee_factory = EmployeeFactory()
        print_service = PrintEmployeeService()
        try:
            file_name = input('Please enter which file you would like to access (employees1-employees5): ')
            # Creates a lookup dictionary with Manager and Employee objects
            employees_lookup_dict = employee_factory.create(file_path=f'./resources/{file_name}.json')
            # Sets and prints office hierarchy
            print_service.execute(employees_lookup_dict)
            print_again = input('Would you like to print another file?: (y/n)').lower()
            if print_again == 'n':
                print('See you next time!')
                break
        except FileNotFoundError as e:
            print(f'[Util {__name__}] File not found: {e}')


if __name__ == '__main__':
    print_office_hierarchy()
