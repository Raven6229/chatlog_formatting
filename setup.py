#!usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", "r") as reqs:
    requirements = reqs.readlines()

setup(
    name = "chatlog_formatting",
    version = "0.0.0",
    description = "",
    author = "Raven6229",
    install_requires = requirements,
    author_email = "",
    packages = find_packages(),
    scripts = []
)