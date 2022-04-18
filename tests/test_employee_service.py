import pytest

from src.entity.Employee import EmployeeBase
from src.service.EmployeeService import EmployeeService


def test_total_salary():
    """
    Assert total salary of employee_dict
    :return: None
    """
    employee_dict = {
        1: EmployeeBase(employee_id=1, first_name="Jean", manager=0, salary=100000),
        2: EmployeeBase(employee_id=2, first_name="Kevin", manager=1, salary=100000),
        3: EmployeeBase(employee_id=3, first_name="KB", manager=1, salary=100000),
        4: EmployeeBase(employee_id=4, first_name="Athena", manager=2, salary=100000),
        5: EmployeeBase(employee_id=5, first_name="Selena", manager=3, salary=100000)
    }

    service = EmployeeService()
    assert service.set_total_salary(employee_dict)
