#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    u_list = []
    for x in my_list:
        if x not in u_list:
            u_list.append(x)
    for x in range(0, len(u_list)):
        sum = sum + u_list[x]
    return sum
