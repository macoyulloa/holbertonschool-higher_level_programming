#!/usr/bin/python3
def average(my_list=[]):
    suma = 0
    prom = 0
    leng = len(my_list)
    for i in range(0, leng):
        suma = suma + my_list[i]
    prome = suma / leng
    return prome
