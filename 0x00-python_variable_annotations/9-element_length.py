#!/usr/bin/env python3
"""
9-element_length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    gets the length of an element from an iterable
    Arg:
        lst: iterable
    Return:
        a list of tuple containing both the element and its length
    """
    return [(i, len(i)) for i in lst]
