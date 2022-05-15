"""
Unit test:

"""
import pytest

from office_hierarchy.entity.Employee import Manager, Employee
from office_hierarchy.entity.EmployeeFactory import EmployeeFactory
from office_hierarchy.service.PrintEmployeeService import PrintEmployeeService


# when open_file is called, it will return the _open_file, which will then return service
# try with lazy fixtures
@pytest.fixture(scope='function')
def open_file():
    def _open_file(file_path):
        employee_factory = EmployeeFactory()
        return employee_factory.create(file_path=file_path)
    return _open_file


@pytest.mark.parametrize('input_file_path', ['tests/data/error_empty_json_file.json'])
def test_empty_json_file_error(input_file_path, open_file):
    """
    Tests empty json file
    :param input_file_path: str
    :param open_file: fixture
    :return: None
    """
    with pytest.raises(TypeError):
        print_service = PrintEmployeeService()
        employees = open_file(file_path=input_file_path)
        assert not print_service.execute(employees)


@pytest.mark.parametrize('input_file_path', ['tests/data/employees2.json'])
def test_number_of_employees(input_file_path, open_file):
    """
    Test number of employees field in EmployeeService
    """
    print_service = PrintEmployeeService()
    employees = open_file(file_path=input_file_path)
    print_service.execute(employees)
    number_of_employees = len(employees)
    assert number_of_employees == 5


@pytest.mark.parametrize('input_file_path', ['tests/data/employees5.json'])
def test_employee_type(input_file_path, open_file):
    """
    Test employee type with lookup_employee_dict field in EmployeeService
    """
    print_service = PrintEmployeeService()
    employees = open_file(file_path=input_file_path)
    print_service.execute(employees)
    jeff_manager = employees.get(2)
    andy_employee = employees.get(203)
    assert isinstance(jeff_manager, Manager)
    assert isinstance(andy_employee, Employee)


@pytest.mark.parametrize('input_file_path', ['tests/data/error_no_top_manager.json'])
def test_no_top_manager(capsys, input_file_path, open_file):
    """
    Test no top manager
    :return: None
    """
    print_service = PrintEmployeeService()
    employees = open_file(file_path=input_file_path)
    result = print_service.execute(employees)
    captured = capsys.readouterr()
    assert not result
    assert 'TypeError: No top manager found' in captured.out

