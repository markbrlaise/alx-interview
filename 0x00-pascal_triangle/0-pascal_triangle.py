#!/usr/bin/python3


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def pascal_triangle(n):
    if n <= 0:
        return []

    def pascal(n):
        c = 1
        row = []
        for j in range(0, n+1):
            c = fact(n) // ((fact(n - j) * fact(j)))
            row.append(c)

        return row

    return [pascal(row) for row in range(n)]
