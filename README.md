# code-katas
CodeFellows 401, Codewars.com Katas

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

I solved this kata by using the Binary Heap data structure.  I loaded every billionaire under 80 into it.  The first one popped from the list was the youngest and the last one popped was the oldest.

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