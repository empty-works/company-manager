'''
Abstract employee class
'''
from abc import ABCMeta

class Employee(metaclass=ABCMeta):
    
    def __init__(self, name = 'N/A'):
        self.name = name
        self.rate = 0.00

    def hire(self):
        pass
    
    def fire(self):
        pass

    def raise(self):
        pass
