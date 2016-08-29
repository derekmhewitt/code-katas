# -*- coding: utf-8 -*-
"""File tests sort_cards.py kata."""
from __future__ import unicode_literals
from sort_cards import sort_cards


def test_sort_cards_one():
    assert sort_cards(list('39A5T824Q7J6K')) == list('A23456789TJQK')


def test_sort_cards_two():
    assert sort_cards(list('Q286JK395A47T')) == list('A23456789TJQK')


def test_sort_cards_three():
    assert sort_cards(list('54TQKJ69327A8')) == list('A23456789TJQK')
