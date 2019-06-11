#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return super().height

    @size.setter
    def size(self, value):
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)

    def __str__(self):
        a = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return(a.format(self.id, self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        args_list = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        i = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return i
