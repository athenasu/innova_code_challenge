"""
Can send error metrics to AWS CloudWatch
"""


class EmployeeError(Exception):
    pass


class EmployeeTypeError(Exception):
    pass


class EmployeeIOError(Exception):
    pass
