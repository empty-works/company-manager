'''
Abstract employee class
'''
from abc import ABCMeta

class Employee(metaclass=ABCMeta):
    
    def __init__(self, id_num, name = 'N/A'):
        self.id_num = id_num
        self.name = name
        self.rate = 0.00
        self.hours_per_day = 0

    def get_id(self):
        return self.id_num

    def get_name(self):
        return self.name

    def get_rate(self):
        return self.rate

    def get_hours(self):
        return self.hours_per_day

    def raise_pay(self):
        pass
