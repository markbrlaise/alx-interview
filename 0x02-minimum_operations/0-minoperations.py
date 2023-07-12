#!/usr/bin/python3
"""module to find minimum number of operations
"""


def minOperations(n):
    """function to find mini operations to copy paste 'H' n times
    """
    sum = 0

    def get_factor(n):
        # function to get smallest factor after 1
        if n <= 1:
            return 0
        elif n > 1:
            for i in range(2, n+1):
                if (n % i) == 0:
                    n = int(n / i)
                    return i + get_factor(n)

    sum += get_factor(n)

    return sum
