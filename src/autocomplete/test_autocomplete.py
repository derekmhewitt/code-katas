"""This file tests the callable AutoCompleter class found in
autocomplete.py

Some of the test formats here were found in the assignment posting."""
from __future__ import unicode_literals
import pytest

TEST_LIST = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']


def test_autocomplete_init_correct_inputs():
    """Test AutoCompleter class w/ correct inputs."""
    from .autocomplete import AutoCompleter
    test_list = ["yellow", "blue", "green"]
    test_case = AutoCompleter(test_list)
    assert test_case.word_list == test_list


def test_autocomplete_init_input_not_list():
    """Test AutoCompleter class with input that isn't a list."""
    from .autocomplete import AutoCompleter
    test_list = {}
    with pytest.raises(TypeError) as message:
        AutoCompleter(test_list)
    assert "AutoCompleter only accepts inputs inside a Python list." in str(message)


def test_autocomplete_init_empty_list():
    """Test AutoCompleter class with an empty list."""
    from .autocomplete import AutoCompleter
    test_list = []
    test_case = AutoCompleter(test_list)
    assert test_case.word_list == []


def test_autocomplete_init_input_not_strings_in_list():
    """Test AutoCompleter init with improper input."""
    from .autocomplete import AutoCompleter
    test_list = [1, 5, 8]
    with pytest.raises(TypeError) as message:
        AutoCompleter(test_list)
    assert "All the items in your list must be strings." in str(message)


def test_autocomplete_init_input_max_completeions():
    """Verify that max completions keyword arg inits correctly."""
    from .autocomplete import AutoCompleter
    test_list = []
    test_case = AutoCompleter(test_list, max_completions=12)
    assert test_case.max_completions == 12


def test_autocomplete_call_with_not_string():
    """Verify that AutoCompleter throws correct error if called without
    a string as argument."""
    from .autocomplete import AutoCompleter
    test_list = ["yellow"]
    test_case = AutoCompleter(test_list)
    with pytest.raises(TypeError) as message:
        test_case(13)
    assert "You must input a string." in str(message)


def test_autocomplete_call_with_3_words():
    """Verify that AutoCompleter hands back whole words."""
    from .autocomplete import AutoCompleter
    test_list = ['apple', 'strawberry', 'pineapple']
    test_case = AutoCompleter(test_list)
    output = test_case("apple")
    assert output == ["apple"]


def test_autocomplete_call_with_f():
    """Verify that AutoCompleter hands back 4 outputs when it's told
    to only hand back 4."""
    from .autocomplete import AutoCompleter
    test_case = AutoCompleter(TEST_LIST, max_completions=4)
    output = test_case("f")
    assert len(output) == 4


def test_autocomplete_call_with_fi():
    """Verify that AutoCompleter finds all 5 matching words."""
    from .autocomplete import AutoCompleter
    test_case = AutoCompleter(TEST_LIST)
    output = test_case("fi")
    assert len(output) == 5


def test_autocomplete_call_with_fin():
    """Verify that AutoCompleter finds all 3 matching words."""
    from .autocomplete import AutoCompleter
    test_case = AutoCompleter(TEST_LIST)
    output = test_case("fin")
    assert len(output) == 3
    assert "final" in output


def test_autocomplete_call_with_finally():
    """Verify that AutoCompleter hands back an empty list if word is
    not found in it's trie."""
    from .autocomplete import AutoCompleter
    test_case = AutoCompleter(TEST_LIST)
    output = test_case("finally")
    assert len(output) == 0
