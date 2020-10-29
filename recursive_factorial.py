"""
This file contains implementation of recursively getting the factorial of an integer.
Author: DtjiSoftwareDeveloper
"""


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))  # 720
print(factorial(5))  # 120
print(factorial(4))  # 24
print(factorial(3))  # 6
