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
