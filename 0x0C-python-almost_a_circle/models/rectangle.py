#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def w_h_valid(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def x_y_valid(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.w_h_valid("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.w_h_valid("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.x_y_valid("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.x_y_valid("y", value)
        self.__y = value
