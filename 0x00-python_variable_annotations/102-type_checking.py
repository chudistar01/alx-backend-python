#!/usr/bin/env python3
""" Duck typing - first element """
from typing import Tuple, List, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List:
    """Zoom array"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
