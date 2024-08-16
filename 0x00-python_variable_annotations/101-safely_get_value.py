#!/usr/bin/env python3
""" Duck typing - first element """
from typing import Any, Union, Sequence, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """ get value """
    if key in dct:
        return dct[key]
    else:
        return default
