# -*- coding: utf-8 -*-
"""This file contains a solution to a codewars kata."""


def series_sum(n):
    """Function solves the above kata.

    Working file was "sum_of_first_nth.py"
    """
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"
    elif n == 2:
        return "1.25"
    else:
        terms = [1, .25]
        n = n - 2
        for i in range(n):
            terms.append(1 / (4 + n * 3))
            n = n - 1
        print(terms)
        return str(("{0:.2f}".format(sum(terms))))
