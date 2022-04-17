from service.EmployeeService import EmployeeService


def print_office_hierarchy():
    service = EmployeeService()
    file_number = input('Please enter which file you would like to access (numbers 1-4): ')
    service.execute(json_filename=f'employees{file_number}.json')


if __name__ == '__main__':
    print_office_hierarchy()
