#!/usr/bin/env python3
"""
100-safely_get_value
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    safely gets the value from a dictionary
    Args:
        dct: dictionary
        key: key to search from dictionary
        default: default return value
    Return:
        value of the key if key in dictionary, else default
    """
    if key in dct:
        return dct[key]
    else:
        return default
