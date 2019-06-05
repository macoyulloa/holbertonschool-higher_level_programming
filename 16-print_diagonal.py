#!/usr/bin/python3
def print_diagonal(n):
    j = 0
    for i in range(0, n):
        if i == j:
            print("\\")
        elif j < i:
            for x in range(0, i):
                print(" ", end="")
        elif n <= 0:
            print("")
