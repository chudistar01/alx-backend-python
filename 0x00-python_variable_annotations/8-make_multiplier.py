#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import Union, List, Callable, Iterator, Optional, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        """multiplies a float by multiplier"""
        return float(n * multiplier)

    return f
