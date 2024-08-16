#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of float and integer as arguement and
    returns their sum as a float
    """
    return float(sum(mxd_lst))
