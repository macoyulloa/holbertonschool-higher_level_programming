#!/usr/bin/python3
def validez_tuple(tuple_val=()):
    if len(tuple_val) == 0:
        return ((0, 0))
    elif len(tuple_val) == 1:
        tuple_val = list(tuple_val)
        tuple_val.append(0)
        tuple_val = tuple(tuple_val)
    return tuple_val


def add_tuple(tuple_a=(), tuple_b=()):
    a = validez_tuple(tuple_a)
    b = validez_tuple(tuple_b)
    return (a[0] + b[0], a[1] + b[1])
