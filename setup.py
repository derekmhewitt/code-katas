# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="code-katas",
    description="Code Fellows 401 Python Code Katas",
    version=0.1,
    author="Derek Hewitt",
    author_email="derekmhewitt@gmail.com",
    license="MIT",
    py_modules=["code-katas"],
    package_dir={"": "src"},
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
        ]
    }
)
