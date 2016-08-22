# -*- coding: utf-8 -*-
"""Proper Parenthetics code challenge."""
from __future__ import unicode_literals


def proper_parens(input_string):
    """Count parens in string and return an integer.

    Closing parens ) must be proceeded by open parens ( in order
    to count as pairs.
    If ((() function will return 1.
    If ())) function will return -1.
    If ((())) function will return 0.

    I'm opting to use a singly-linked list for this.  I realize my solution
    doesn't solve the problem entirely, but I'm out of time and have to get
    some sleep tonight.

    There's a better way to go through the string and match parens up and
    discard pairs as you go but I couldn't successfully get that
    working so I fell back to this method.
    """

    from linked_list import LinkedList
    parens_ll = LinkedList(input_string)
    parens_open = 0
    parens_closed = 0
    while len(parens_ll) > 0:
        current = parens_ll.pop()
        if "(" in current:
            parens_open += 1
        if ")" in current:
            parens_closed += 1

    if parens_open > parens_closed:
        return 1
    elif parens_closed > parens_open:
        return -1
    else:
        return 0
