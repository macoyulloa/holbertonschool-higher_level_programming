#!/usr/bin/python3
class MyClass:
    """ My class
    """
       
    def __init__(self, name):
        self.__name = name
        self.__number = 0
                              
    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
