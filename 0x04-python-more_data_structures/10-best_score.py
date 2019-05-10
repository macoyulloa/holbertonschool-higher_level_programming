#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    inverse = [(value, key) for key, value in a_dictionary.items()]
    return max(inverse)[1]
