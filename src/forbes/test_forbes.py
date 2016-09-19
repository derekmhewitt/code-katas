# -*- coding: utf-8 -*-

"""Test forbes.py code."""
from __future__ import unicode_literals

BILLIONAIRES_FILENAME = "./forbes_billionaires.json"

TEST_BILLIONAIRE = """{
    "name": "Amancio Ortega",
    "age": 80,
    "rank": 2,
    "net_worth (USD)": 67000000000,
    "source": "Zara",
    "country": "Spain"
}"""

TEST_BILLIONAIRES = """[{
        "name": "Warren Buffett",
        "age": 85,
        "rank": 3,
        "net_worth (USD)": 60800000000,
        "source": "Berkshire Hathaway",
        "country": "United States"
    },
    {
        "name": "Carlos Slim Helu",
        "age": 76,
        "rank": 1,
        "net_worth (USD)": 50000000000,
        "source": "telecom",
        "country": "Mexico"
    },
    {
        "name": "Jeff Bezos",
        "age": 52,
        "rank": 5,
        "net_worth (USD)": 45200000000,
        "source": "Amazon.com",
        "country": "United States"
    },
    {
        "name": "Sergey Brin",
        "age": 42,
        "rank": 13,
        "net_worth (USD)": 34400000000,
        "source": "Google",
        "country": "United States"
    }]"""


def test_get_billionaires_from_file():
    """verify that get function opens file and reads data"""
    from forbes import get_billionaires_from_file
    data = get_billionaires_from_file(BILLIONAIRES_FILENAME)
    assert isinstance(data, str)


def test_read_in_data():
    """verify that data is parsed correctly"""
    from forbes import read_in_data
    data = read_in_data(TEST_BILLIONAIRE)
    assert data['name'] == "Amancio Ortega"


def test_process_billionaires():
    """verify that expected billionaires are output as results"""
    from forbes import read_in_data
    from forbes import process_billionaires
    data = read_in_data(TEST_BILLIONAIRES)
    output = process_billionaires(data)
    assert "Sergey Brin" in output
