# -*- coding: utf-8 -*-
"""This file contains the solution to the following kata.

http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/python

Instructions:

Task:

Your task is to write a function which returns the sum of following series
upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:

You need to round the answer upto 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.
Examples:

SeriesSum(1) => 1 = "1"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

I got help with rounding floats here:
http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
"""


def series_sum(n):
    """Function solves the above kata."""
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
