"""Implement an autocomplete funciton in Python using a Trie tree data
structure.

See README for details."""
from __future__ import unicode_literals


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
        from .trie import Trie
        self.tree = Trie()
        output = []
        for word in self.word_list:
            self.tree.insert(word)
        match_list = list(match)
        tree = self.tree.words
        reconstruct = ""
        for letter in match_list:
            try:
                if tree[letter]:
                    reconstruct += letter
                    tree = tree[letter]
            except KeyError:
                return output
        gen = self.tree.traverse()
        for word in gen:
            if word.find(reconstruct) == 0:
                output.append(word)
            if len(output) == self.max_completions:
                break
        return output
