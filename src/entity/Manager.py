'''
Manager class that inherits from EmployeeBase
'''

from src.entity.EmployeeBase import EmployeeBase
from src.entity.Employee import Employee


class Manager(Employee):
    team_members: list[EmployeeBase] = []
