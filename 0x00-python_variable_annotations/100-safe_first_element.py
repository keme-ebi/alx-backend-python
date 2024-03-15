#!/usr/bin/env python3
"""
100-safe_first_element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    gets the first element from a sequence
    Arg:
        lst(sequence[any]): can be a list of any type
    Return:
        the first element from lst if lst is not empty, else None
    """
    if lst:
        return lst[0]
    else:
        return None
