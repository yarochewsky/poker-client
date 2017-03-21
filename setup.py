import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Deuces Poker Client",
    version = "1.0",
    author = "Daniel Fonseca Yarochewsky",
    description = ("A client to simulate a Texa Holdem Poker Table"),
    license = "Free",
    packages=['deuces-master', 'termcolor'],
    long_description=read('README')
)
