'''
Manager class that inherits from EmployeeBase
'''

from typing import Optional
from pydantic import BaseModel, validator
import re


class EmployeeBase(BaseModel):

    employee_id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    # Validate first_name attribute
    @validator("first_name")
    def first_name_must_be_alphabet(cls, v):
        first_name_format = re.compile("^[A-Z][-a-zA-Z]+$")
        if first_name_format.match(v):
            return v
        raise TypeError('TypeError: First name must only include alphabets from A-Z')


class Employee(EmployeeBase):
    level: int = 0


class Manager(Employee):
    team_members: list[EmployeeBase] = []
