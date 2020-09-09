'''
Abstract employee class
'''
from abc import ABCMeta

class Employee(metaclass=ABCMeta):
    
    def __init__(self, name = 'N/A', salary = 100000.00):
        self.name = name
        self.salary = salary

class HourlyEmployee(Employee):
    pass

class SalariedEmployee(Employee):
    pass

class Manager(Employee):
    pass

class Executive(Employee):
    pass
