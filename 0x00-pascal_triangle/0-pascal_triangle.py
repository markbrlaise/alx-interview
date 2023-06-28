#!/usr/bin/python3
"""Pascal's triangle interview challenge"""


def fact(n):
    """return the factorial of an integer to help
    us get the coefficients"""
    if n == 0:
        return 1
    return n * fact(n - 1)


def pascal_triangle(n):
    """returns a list of lists representing
    pascal's triangle"""
    if n <= 0:
        return ['']

    def pascal(n):
        """returns a list of a row"""
        c = 1
        row = []
        for j in range(0, n+1):
            # getting and appending the coeffients to the row
            c = fact(n) // ((fact(n - j) * fact(j)))
            row.append(c)

        return row

    return [pascal(row) for row in range(n)]
