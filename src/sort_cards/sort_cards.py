# -*- coding: utf-8 -*-
"""File implements a solution to card sorting kata."""
from __future__ import unicode_literals
from operator import itemgetter


def sort_cards(cards):
    """This function takes in a list of card names (list must contain at least
    one card) and returns it sorted by value, Ace being lowest.

    Sources used to complete this kata:
    https://wiki.python.org/moin/HowTo/Sorting, specifically the
    "Operator Module Functions" section.
    """

    cards_dict = {
        "A": ("A", 1),
        "2": ("2", 2),
        "3": ("3", 3),
        "4": ("4", 4),
        "5": ("5", 5),
        "6": ("6", 6),
        "7": ("7", 7),
        "8": ("8", 8),
        "9": ("9", 9),
        "T": ("T", 10),
        "J": ("J", 11),
        "Q": ("Q", 12),
        "K": ("K", 13)
    }
    first_list = []
    for i in cards:
        first_list.append(cards_dict.get(i))
    sorted_list = sorted(first_list, key=itemgetter(1))
    return_list = []
    for i in sorted_list:
        return_list.append(i[0])
    return return_list
