#!/usr/bin/env python3
"""
7-to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    adds two values to a tuple
    Args:
        k(str): string
        v(int or float): int or float squared
    Return:
        a tuple of both values, with k as first element and v as last
    """
    tup: Tuple[str, float] = (k, v ** 2)
    return tup
