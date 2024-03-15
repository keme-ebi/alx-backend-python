#!/usr/bin/env python3
"""
102-type_checking
"""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    doubles the numbers from a tuple
    Arg:
        lst: tuple to go through
        factor: number of times each number of element should be listed
    Return:
        list of zoomed array
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
