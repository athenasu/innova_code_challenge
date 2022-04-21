'''
Three classes: EmployeeBase, Employee, Manager
Manager class implements Employee class, which implements EmployeeBase class
'''

from typing import Optional
from pydantic import BaseModel, validator
import re

RE_FIRST_NAME_FORMAT = re.compile("^[A-Z][-a-zA-Z]+$")


class EmployeeBase(BaseModel):
    """
    EmployeeBase class implements pydantic's BaseModel to validate fields
    """
    employee_id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    # Validate first_name attribute compared to global regex variable
    @validator("first_name")
    def first_name_must_be_alphabet(cls, v):
        if RE_FIRST_NAME_FORMAT.match(v):
            return v
        raise TypeError('TypeError: First name must only include alphabets from A-Z')


class Employee(EmployeeBase):
    """
    Employee class implements EmployeeBase
    level: keeps track of each employee's level in the company, will also be used to show indentation
    """
    level: int = 0


class Manager(Employee):
    """
    Manager class implements Employee class
    team_members: stores the list of their
    """
    team_members: list[EmployeeBase] = []
