#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    inverse = [(value, key) for key, value in a_dictionary.items()]
    for i, j in sorted(inverse.items()):
        if i == value:
            a_dictionary.pop(None, value)
    return a_dictionary
