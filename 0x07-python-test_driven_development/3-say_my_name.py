#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """function that prints my name.

    Args:
        first_name (str): first name.
        last_name (str): last name.

    Returns:
        The function need to return the name.

    .. _PEP8:
        Style correction

    """
    for i in range(len(first_name)):
        if type(first_name[i]) != str:
            raise TypeError("first_name must be a string") from e
    for i in range(len(last_name)):
        if type(last_name[i]) != str:
            raise TypeError("last_name must be a string") from e
    print("My name is {} {}".format(first_name, last_name))
