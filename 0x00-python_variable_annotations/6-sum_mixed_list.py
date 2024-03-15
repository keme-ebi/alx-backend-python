#!/usr/bin/env python3
"""
6-sum_mixe_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sums up the values in a mixed list of integers and floats
    Arg:
        mxd_list(Union[int, float]): mixed list of integers and floats
    Return:
        sum of the values in the list
    """
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
