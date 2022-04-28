"""
Main function that calls EmployeeService
"""
from office_hierarchy.service.PrintEmployeeService import PrintEmployeeService


def print_office_hierarchy():
    """
    Interactive method to choose which files to access
    Calls EmployeeService's execute method
    :return: None
    """

    while True:
        service = PrintEmployeeService()
        file_name = input('Please enter which file you would like to access (employees1-employees5): ')
        service.execute(file_path=f'./resources/{file_name}.json')
        print_again = input('Would you like to print another file?: (y/n)').lower()
        if print_again == 'n':
            print('See you next time!')
            break


if __name__ == '__main__':
    print_office_hierarchy()
