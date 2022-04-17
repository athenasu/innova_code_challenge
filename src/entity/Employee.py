'''
Manager class that inherits from EmployeeBase
'''

from typing import Optional
from pydantic import BaseModel, ValidationError, validator


class EmployeeBase(BaseModel):

    employee_id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    # try with first name & regular expressions
    @validator("employee_id")
    def id_must_be_integer(cls, v):
        try:
            isinstance(v, int)
            return v
        except ValidationError:
            raise ValueError("Id must be integer")


class Employee(EmployeeBase):
    level: int = 0


class Manager(Employee):
    team_members: list[EmployeeBase] = []
