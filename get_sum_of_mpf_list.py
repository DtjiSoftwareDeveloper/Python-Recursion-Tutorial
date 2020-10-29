"""
This file contains implementation of calculating the mpf sum of an mpf list.
Author: DtjiSoftwareDeveloper
"""


from mpmath import *


# Creating a function to check whether a string is a number or not


def is_number(a_string: str) -> bool:
    try:
        mpf(a_string)
        return True
    except ValueError:
        return False


# Creating a function to calculate the mpf sum of an mpf list


def sum_of_mpf_list(a_list: list) -> mpf:
    if len(a_list) == 0:
        return mpf("0")
    elif len(a_list) == 1:
        if is_number(a_list[0]):
            return mpf(str(a_list[0]))
        else:
            return mpf("0")
    else:
        if is_number(a_list[0]):
            return mpf(str(a_list[0])) + sum_of_mpf_list(a_list[1::])
        else:
            return mpf("0") + sum_of_mpf_list(a_list[1::])


# Test code
a_list: list = [mpf("5.53"), 7.23, 8]
print(sum_of_mpf_list(a_list))  # 20.76
b_list: list = ["xx", 5.53, mpf("7.23"), 8, "cc"]
print(sum_of_mpf_list(b_list))  # 20.76
print(sum_of_mpf_list(a_list) == sum_of_mpf_list(b_list))  # True
