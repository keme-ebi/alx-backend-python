#!/usr/bin/env python3
"""
5-sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sums the values of floats from a list
    Arg:
        input_list(list[float]): a list of floats
    Return:
        sum of the floats in the list
    """
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
