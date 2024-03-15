#!/usr/bin/env python3
"""
8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    makes a multiplier
    Arg:
        multiplier(float): float to multiply
    Return:
        function that multiplies the float
    """
    def multiply(num: float) -> float:
        """
        multiplies the float
        Arg:
            num(float): float
        Return:
            multiplied floats
        """
        return num * multiplier
    return multiply
