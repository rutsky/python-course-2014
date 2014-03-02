# rndcolors3.py
from random import choice

__all__ = ["random_color"]

colors = ["red", "green", "blue"]

def random_color():
    return random.choice(colors)
