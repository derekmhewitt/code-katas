# -*- coding: utf-8 -*-
"""Tests for Proper Parenthetics code challenge."""
import pytest

PARENTHETIC_TESTS = [
    (("This is a () weird string( with )some parenthesis()"
     "that is balanced()."), 0),
    ("This is ))) a broken string )))(()).", -1),
    ("This ((( string is (())(( open.", 1)
]


@pytest.mark.parametrize("string, return_value", PARENTHETIC_TESTS)
def test_proper_parens(string, return_value):
    from proper_parenthetics import proper_parens
    assert proper_parens(string) is return_value
