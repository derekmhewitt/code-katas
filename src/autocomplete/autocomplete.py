"""Implement an autocomplete funciton in Python using a Trie tree data
structure."""
from __future__ import unicode_literals
"""
Your Task:
Write a callable Python class which will implement autocomplete functionality. Your class should take a list of words to be a vocabulary as an argument on initialization. It should also accept a max_completions argument, which controls the maximum number of suggested completions for a given string. The max_completions argument should default to 5.

The input to the call method for the class will be the string the user has typed. When called, this class should return a list of at most max_completions suggested words. If there are more available completions than allowed, you are free to decide which to return. If there are no completions available, you should return an empty list. Your class should handle inappropriate inputs correctly.

In the end, your class should be usable like so:

"""


class AutoCompleter(object):
    """Callable class that takes in a string from the user and returns
    a list of words that match from the list it was fed when the
    instance of the class was initialized."""

    def __init__(self, word_list, max_completions=5):
        """Init method for our callable class."""
        if not isinstance(word_list, list):
            raise TypeError("AutoCompleter only accepts inputs inside a Python list.")
        for item in word_list:
            if not isinstance(item, str):
                raise TypeError("All the items in your list must be strings.")
        self.word_list = word_list
        self.max_completions = max_completions

    def __call__(self, match):
        """Call method for our callable class.  Returns a list of words that
        match the input string we initialized the class with."""
        if not isinstance(match, str):
            raise TypeError("You must input a string.")
        from trie import Trie
        self.tree = Trie()
        for word in self.word_list:
            self.tree.insert(word)
