#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    suma = 0
    for i in range(0, x):
        try:
            print(my_list[suma], end="")
            suma += 1
        except:
            pass
    print('')
    return suma
