'''
Three classes: EmployeeBase, Employee, Manager
Manager class implements Employee class, which implements EmployeeBase class
'''

from typing import Optional
from pydantic import BaseModel, validator
import re


class EmployeeBase(BaseModel):
    """
    EmployeeBase class implements pydantic's BaseModel to validate fields
    """
    employee_id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    # Validate first_name attribute with python .isalpha() method
    @validator("first_name")
    def first_name_must_be_alphabet(cls, v):
        if v.isalpha():
            return v
        raise TypeError('TypeError: First name must only include alphabets from A-Z')


class Employee(EmployeeBase):
    """
    Employee class implements EmployeeBase
    """
    # keeps track of each employee's level in the company, will also be used to show indentation
    level: int = 0


class Manager(Employee):
    """
    Manager class implements Employee class
    """
    # stores the list of Manager's team members
    team_members: list[EmployeeBase] = []
