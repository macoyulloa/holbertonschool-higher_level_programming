#!/usr/bin/python3
" Module rectangle.py - from base "
from models.base import Base


class Rectangle(Base):
    " Class inheritance from base "
    def __init__(self, width, height, x=0, y=0, id=None):
        " Init "
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def w_h_valid(self, name, value):
        " validations of the atributes "
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def x_y_valid(self, name, value):
        " Validations of the atributes "
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        " Width getter "
        return self.__width

    @property
    def height(self):
        " Height getter "
        return self.__height

    @property
    def x(self):
        " x getter "
        return self.__x

    @property
    def y(self):
        " y getter "
        return self.__y

    @width.setter
    def width(self, value):
        " width setter "
        self.w_h_valid("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        " height setter "
        self.w_h_valid("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        " x setter "
        self.x_y_valid("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        " y setter "
        self.x_y_valid("y", value)
        self.__y = value

    def area(self):
        " Funtion return the area of the rectangle "
        return self.width * self.height

    def display(self):
        " Print the char of the rectangle size "
        for k in range(self.y):
            print()
        for i in range(0, self.height):
            print(' ' * self.x, end='')
            for j in range(0, self.width):
                print("{}".format('#'), end='')
            print()

    def __str__(self):
        " Funtion that prints a representation "
        a = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return(a.format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        " Funtion to update the dictionary with the atributes "
        args_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        " Function to get the dictionary "
        dict_list = {}
        dict_list['id'] = self.id
        dict_list['width'] = self.width
        dict_list['height'] = self.height
        dict_list['x'] = self.x
        dict_list['y'] = self.y
        return dict_list
