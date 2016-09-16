# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""This file contains an algorithym and supporting functions for finding the
distance between various airports defined in the cities_with_airports.json
file located in the same directory."""

import math
import json
from graph import Graph

AIRPORTS_FILE = "cities_with_airports.json"


def calculate_distance(point1, point2):
    """
    Provided by Nick to help solve this problem.

    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def get_airports_from_file(filename):
    with open(filename) as file:
        return file.read()


def read_in_data(data):
    return json.loads(data)


    """
    This is one city in the json file

    {"city": "Goma",
    "connection_urls": [
    "https://en.wikipedia.org/wiki/Kindu_Airport",
    "https://en.wikipedia.org/wiki/Bangoka_International_Airport",
    "https://en.wikipedia.org/wiki/N%27djili_Airport",
    "https://en.wikipedia.org/wiki/Addis_Ababa_Bole_International_Airport"
    ],
    "url": "https://en.wikipedia.org/wiki/Goma_International_Airport",
    "country": "Democratic Republic of the Congo",
    "destination_cities": [
    "Kinshasa", "Kisangani", "Addis Ababa"
    ],
    "destination_airports": [
    "N'djili Airport", "Bangoka International Airport",
    "Addis Ababa Bole International Airport"
    ],
    "airport": "Goma International Airport",
    "lat_lon": [-1.669889, 29.238278]}
    """


def create_graph(data_blob):
    graph = Graph()
    for entry in data_blob:
        graph.add_node(entry["city"])
    """
    So I'm stumped at this point..  I got the data read in and can iterate
    through it ok.

    I know that next I need to create edges for each
    city in the graph that are weighted according to their distance.  But
    the entries in the json don't have a key, they're just a list of dicts.
    For my example above I'm at the airport 'Goma' and I need to look up
    each of the other airports in 'destination_cities' and use their lat/long
    and the one I already have for Goma
    in order to weight that edge.  But since there's no key on the dict they're
    in for me to search for, how do I get ahold of the particular dict that
    city "X" is in without it having a key on the outside of it?
    """

if __name__ == '__main__':
    data = get_airports_from_file(AIRPORTS_FILE)
    airports_blob = read_in_data(data)
    graph = create_graph(airports_blob)
    print(graph.shortest_path('Pointe Vele Airport', 'Hihifo Airport'))
