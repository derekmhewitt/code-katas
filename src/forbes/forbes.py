# -*- coding: utf-8 -*-
"""Assignment Description:

Write a function that,
returns the name, net worth, and industry of the **oldest billionaire
under 80 years old** AND the youngest billionaire with a valid age. *
Oldest under 80, not including 80. * You may not use a sorting function.
* You may not use any external library (you don’t need it)."""

from __future__ import unicode_literals
import json
from heap import Heap

BILLIONAIRES_FILENAME = "forbes_billionaires.json"


def get_billionaires_from_file(filename):
    """opens filename from argument and reads in the data"""
    with open(filename) as file:
        return file.read()


def read_in_data(data):
    return json.loads(data)


def process_billionaires(data):
    heap = Heap()
    for bill in data:
        if bill['age'] < 80 and bill['age'] > 0:
            heap.push(bill['age'])
    results = []
    try:
        while True:
            results.append(heap.pop())
    except IndexError:
        pass
    youngest = results[0]
    oldest = results[-1]
    for bill in data:
        if bill['age'] == youngest:
            youngest_name = bill['name']
        if bill['age'] == oldest:
            oldest_name = bill['name']
    output = "The youngest billionaire in our list is {} and the oldest is {}.".format(youngest_name, oldest_name)
    print(output)
    return youngest_name, oldest_name

if __name__ == '__main__':
    data = get_billionaires_from_file(BILLIONAIRES_FILENAME)
    billions_data = read_in_data(data)
    process_billionaires(billions_data)
