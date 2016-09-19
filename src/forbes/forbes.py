# -*- coding: utf-8 -*-
"""Assignment Description:

Write a function that,
returns the name, net worth, and industry of the **oldest billionaire
under 80 years old** AND the youngest billionaire with a valid age. *
Oldest under 80, not including 80. * You may not use a sorting function.
* You may not use any external library (you don’t need it)."""

import json

BILLIONAIRES_FILENAME = "forbes_billionaires.json"


def get_billionaires_from_file(filename):
    """opens filename from argument and reads in the data"""
    with open(filename) as file:
        return file.read()


def read_in_data(data):
    return json.loads(data)



if __name__ == '__main__':
    data = get_billionaires_from_file(BILLIONAIRES_FILENAME)
    billions_data = read_in_data(data)
