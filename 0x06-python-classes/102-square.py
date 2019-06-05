#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        try:
            if not type(size) == int:
                raise TypeError
        except TypeError as e:
            raise Exception("size must be and integer") from e
        try:
            if (int(size) < 0):
                raise ValueError
            self.__size = size
        except ValueError as e:
            raise Exceaption("size must be >= 0") from e

    def area(self):
        return self.__size * self.__size

    def size(self):
        return self.__size

    def size(self, value):
        try:
            if not type(value) == int:
                raise TypeError
        except TypeError as e:
            raise Exception("size must be and integer") from e
        try:
            if (int(value) < 0):
                raise ValueError
            self.__size = value
        except ValueError as e:
            raise Exceaption("size must be >= 0") from e
