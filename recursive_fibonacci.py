"""
This file contains implementation of recursively calculating the nth Fibonacci number.
Author: DtjiSoftwareDeveloper
"""


def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))  # 1
print(fibonacci(3))  # 2
print(fibonacci(4))  # 3
print(fibonacci(5))  # 5
print(fibonacci(6))  # 8
