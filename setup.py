# -*- coding: utf-8 -*-
"""Repo contains the results of my code challenges from Python 401."""
from setuptools import setup

setup(
    name="code-katas",
    description="The results of my code challenges from Python 401.",
    version=0.1,
    author="Derek Hewitt",
    author_email="derekmhewitt@gmail.com",
    license='MIT',
    py_modules=['sum_of_first_nth', 'proper_parenthetics'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
