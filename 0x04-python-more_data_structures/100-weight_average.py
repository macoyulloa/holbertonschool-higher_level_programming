#!/usr/bin/python3
def weight_average(my_list=[]):
    res1 = 0
    res2 = 0
    if my_list:
        for i in my_list:
            res1 += i[0] * i[1]
            res2 += i[1]
        return res1 / res2
    else:
        return 0
