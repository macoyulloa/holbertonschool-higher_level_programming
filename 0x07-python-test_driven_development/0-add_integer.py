#!/usr/bin/python3
def add_integer(a, b=98):
    """function that adds 2 integers.

    Args:
        a (int, Float): The first number
        b (int, Float): The second number

    Returns:
        The function need to return the add of 2 numbers.

    .. _PEP8:
        Style correction

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
