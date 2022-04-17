from src.entity.Employee import Employee
from src.entity.Manager import Manager


class EmployeeFactory:  # pizza factory: https://gist.github.com/aadeshnpn/5652878

    @staticmethod
    def create(employee, manager_ids: list[int]):
        if employee['id'] in manager_ids:
            return Manager(employee_id=employee['id'], first_name=employee['first_name'],
                           manager=employee['manager'], salary=employee['salary'])
        else:
            return Employee(employee_id=employee['id'], first_name=employee['first_name'],
                            manager=employee['manager'], salary=employee['salary'])
