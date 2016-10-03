# code-katas
CodeFellows 401, Codewars.com Katas

## autocomplete

This branch contains a solution for the AutoComplete code kata found here:
https://codefellows.github.io/sea-python-401d4/assignments/kata_autocomplete.html

From that link:
```
Your Task is to:
Write a callable Python class which will implement autocomplete functionality. Your class should take a list of words to be a vocabulary as an argument on initialization. It should also accept a max_completions argument, which controls the maximum number of suggested completions for a given string. The max_completions argument should default to 5.

The input to the call method for the class will be the string the user has typed. When called, this class should return a list of at most max_completions suggested words. If there are more available completions than allowed, you are free to decide which to return. If there are no completions available, you should return an empty list. Your class should handle inappropriate inputs correctly.

In the end, your class should be usable like so:
```
```
>>> from autocomplete import AutoCompleter
>>> vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
>>> complete_me = AutoCompleter(vocabulary, max_completions=4)
>>> complete_me('f')
['fix', 'fax', 'fit', 'fist']
>>> complete_me('fi')
['fix', 'fit', 'fist', 'finch']
>>> complete_me('fin')
['finch', 'final', 'finial']
>>> complete_me('finally')
[]
```

### Cited Sources and Resources:
My Trie tree still has an unresolved bug in it so I used Justin's tree to complete my kata:
https://github.com/welliam/data-structures/tree/trie-traversal

## forbes

This branch contains a solution for the the Forbes Top 40 Billionaires Kata.

The goal of this assignment is to:
```
Write a function that, returns the name, net worth, and industry of the **oldest billionaire under 80 years old** AND the youngest billionaire with a valid age. * Oldest under 80, not including 80. * You may not use a sorting function. * You may not use any external library (you don’t need it).
```

Stretch Goals:
```
Write another function that takes the company owned by the oldest under 80 and youngest billionaire and scrapes the web for its current stock price. If the company is not public, have an appropriate message. If the company is not an actual company, have an appropriate message.
```

I solved this kata by using the Binary Heap data structure.  I loaded every billionaire with an age greater than 0 and less than 80 into it by age.  The first one popped from the list was the youngest and the last one popped was the oldest.

The Heap used here is mine from the Data Structures assignments and I included its tests as well.

### Cited Sources and Resources:
I made good use of http://jsonlint.com/ to find the JSON error in the supplied file, and to setup my test data without errors.

## flight-paths

This branch is an attempt at solving the Flight-Paths kata.

Graph implementation by Justin, from here:
https://github.com/welliam/data-structures/blob/master/src/graph.py

The goal of this assignment is to:
```
Write a function that,

given a starting city and an ending city, will return a path between the two cities (including the two cities).
also returns the total distance traveled between cities.
appropriately handles the situation where no path exists.
```
Stretch Goals:
```
Try to incorporate any (or all) of these. They are/can be independent of each other.

Add to your function a parameter that makes it return the shortest path (lowest distance) between the two cities.
Add to your function a parameter that makes it return the path with the fewest stops between the two cities.
Have your function take a parameter for a limit to the distance between any two cities. If specified, your function returns a path where each city-to-city jump is less than or equal to that limit.
```

I made an attempt at sovling this one and wasn't very successful, my comments are in the flight_paths.py file.


## sort_cards

This branch represents a solution to the Codewars.com card sorting kata found here:

https://www.codewars.com/kata/sort-deck-of-cards/python

Directly quoted from the above link:

```
Description:

Write a function sort_cards() that sorts a shuffled list of cards, so that any given list of cards is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
Hint: Tests will have many occurrences of same rank cards, as well as vary in length. You can assume though, that input list is always going to have at least 1 element.
```

Sources used to complete this kata:
    https://wiki.python.org/moin/HowTo/Sorting, specifically the "Operator Module Functions" section.