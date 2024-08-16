#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import Union, List, Callable, Iterator, Optional, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a list of float and integer as arguement and
    returns their sum as a float
    """

    return (k, v**2)
