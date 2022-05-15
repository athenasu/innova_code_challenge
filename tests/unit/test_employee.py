import pytest
from pydantic import ValidationError

from office_hierarchy.entity.EmployeeError import EmployeeTypeError
from office_hierarchy.entity.EmployeeFactory import EmployeeFactory
from office_hierarchy.service.PrintEmployeeService import PrintEmployeeService


def test_pydantic_validation():  # capsys
    employee_factory = EmployeeFactory()
    print_service = PrintEmployeeService()
    with pytest.raises(EmployeeTypeError):
        employees = employee_factory.create('tests/data/error_pydantic_first_name.json')
        assert not print_service.execute(employees)
    # captured = capsys.readouterr()
    # assert 'TypeError: First name must only include alphabets from A-Z (type=type_error)' in captured.out
