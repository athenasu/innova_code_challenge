import pytest

from office_hierarchy.entity.EmployeeFactory import EmployeeFactory
from office_hierarchy.service.PrintEmployeeService import PrintEmployeeService


DATA_LIST = [
    ('tests/data/employees1.json', True),
    ('tests/data/employees2.json', True),
    ('tests/data/employees3.json', True),
    ('tests/data/employees4.json', True),
    ('tests/data/employees5.json', True),
    ('tests/data/error_no_top_manager.json', False)
]


@pytest.mark.parametrize('test_input, expected', DATA_LIST)
def test_execute(test_input, expected):
    """
    Test execute() method in EmployeeService
    """
    print_service = PrintEmployeeService()
    employee_factory = EmployeeFactory()
    employees = employee_factory.create(file_path=test_input)
    result: bool = print_service.execute(employees)
    assert result is expected
