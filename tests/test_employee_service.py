from src.service.EmployeeService import EmployeeService
from src.entity.Employee import Manager, Employee


def test_execute():
    """
    Test execute() method in EmployeeService
    """
    service = EmployeeService()
    result = service.execute('./resources/employees1.json')
    assert result


def test_number_of_employees():
    """
    Test number of employees field in EmployeeService
    """
    service = EmployeeService()
    service.execute('./resources/employees2.json')
    number_of_employees = len(service.lookup_employee_dict.keys())
    assert number_of_employees == 5


def test_total_salary():
    """
    Test get_total_salary() method in EmployeeService
    """
    service = EmployeeService()
    service.execute('./resources/employees3.json')
    assert service.get_total_salary() == 1070000


def test_employee_level():
    """
    Test employee level in EmployeeService
    """
    service = EmployeeService()
    service.execute('./resources/employees4.json')
    jeff = service.lookup_employee_dict[2]
    dave = service.lookup_employee_dict[1]
    dave_team_members = dave.team_members

    assert jeff.level == 0
    assert dave.level == 1
    assert dave_team_members[0].level == 2


def test_employee_type():
    """
    Test employee type with lookup_employee_dict field in EmployeeService
    """
    service = EmployeeService()
    service.execute('./resources/employees5.json')

    jeff = service.lookup_employee_dict[2]
    andy = service.lookup_employee_dict[203]
    assert isinstance(jeff, Manager)
    assert isinstance(andy, Employee)
