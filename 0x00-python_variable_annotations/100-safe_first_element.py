#!/usr/bin/env python3
""" Duck typing - first element """
from typing import Any, Union, Sequence, Iterable, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ first element """
    if lst:
        return lst[0]
    else:
        return None
