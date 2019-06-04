#!/usr/bin/python3
class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)
