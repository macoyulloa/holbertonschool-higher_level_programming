#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if (isinstance(roman_string, str)) and roman_string:
        return sum(map(lambda x: rom_val[x], roman_string))
    else:
        return 0
