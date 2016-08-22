# -*- coding: utf-8 -*-
"""Proper Parenthetics code challenge."""
from __future__ import unicode_literals
import sys
"""My first programming language was Lisp. If you’re at all familiar with it, you’ll probably know that in Lisp there are a lot of parentheses.

Your assignment is to build a quick Python function incorporating one of this week’s data structures that takes a unicode string (text) as input and returns one of three possible values:

Return 1 if the string is “open” (there are open parens that are not closed)
Return 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
Return -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)
For the purposes of this assignment, open and closed parens must match. As an example, consider this string:

')))((('
Although there are an equal number of open and closed parens, they are not properly paired. This string is “broken”.

Submitting Your Work
Create a proper-parenthetics branch in your code-katas repository. Add this function in a script to your proper-parenthetics branch. The tests that demonstrate your code works should be in a test_parenthetics.py file. Add documentation about your code in the repo’s README.md. Make sure to add notes about and resources or collaborators you worked with in solving this problem.

After you’ve added your code solution into GitHub, send a pull request to your master branch. Submit the link to that pull request to Canvas.

Use the comment box in Canvas to add any questions, comments or reflections on this assignment and your approach to it."""


def proper_parens(input_string):
    """Count parens in string and return an integer.

    Closing parens ) must be proceeded by open parens ( in order
    to count as pairs.
    If ((() function will return 1.
    If ())) function will return -1.
    If ((())) function will return 0.

    I'm opting to use a doubly-linked list for this, because I want to slice
    the input string into managable pieces and parse through them in order.
    The DLL allows me to push into the head and read from the tail easily.


    split string into words and push into data structure
    evaluate each item in there and increment counters, using regular expression?
    """
    sys.path.insert(0, 'data_structures')
    from linked_list import LinkedList
    parens_ll = LinkedList()
    while len(input_string) > 0:
        parens_ll.push(input_string.slice(" ", 1))

    parens_open = 0
    parens_closed = 0

    while len(parens_ll) > 0:
        current = parens_ll.pop()
        if


    return score
