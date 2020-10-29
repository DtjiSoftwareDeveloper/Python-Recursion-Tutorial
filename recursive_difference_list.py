"""
This file contains implementation of creating a new list of differences between two consecutive elements of a list.
Author: DtjiSoftwareDeveloper
"""


def difference_list(a_list: list) -> list:
    if len(a_list) <= 1:
        return []
    else:
        return [int(a_list[0]) - int(a_list[1])] + difference_list(a_list[1::])


# Test code
a: list = [5, 3, 7]
print(difference_list(a))  # [2, -4]
a.append(9)
print(difference_list(a))  # [2, -4, -2]
a.append(2)
print(difference_list(a))  # [2, -4, -2, 7]
a.remove(3)
print(difference_list(a))  # [-2, -2, 7]
