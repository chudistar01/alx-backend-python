#!/usr/bin/env python3
""" Duck typing - first element """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """Zoom array"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
