'''
Abstract employee class
'''
from abc import ABCMeta

class Employee(metaclass=ABCMeta):
    pass

class HourlyEmployee(Employee):
    pass

class SalariedEmployee(Employee):
    pass

class Manager(Employee):
    pass

class Executive(Employee):
    pass
