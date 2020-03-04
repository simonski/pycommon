#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from os import path
from common import constants

VERSION = constants.VERSION

here = path.abspath(path.dirname(__file__))

long_description = "Common classes and functions I use."

setup(
    name="simonski-pycommon",
    version=VERSION,
    description="holds my commonly used classes and functions.",
    long_description=long_description,
    url="https://github.com/simonski/pycommon",
    author="Simon Gauld",
    author_email="simon.gauld@gmail.com",
    license="Apache 2.0",
    classifiers=["Development Status :: 3 - Alpha"],
    keywords="common development",
    python_requires=">=3.6",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[],
    test_suite="tests.test_suite",
)
