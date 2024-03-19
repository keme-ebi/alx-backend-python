#!/usr/bin/env python3
"""
1-async_comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using an async comrehension
        over asyn_generator
    Return:
        list of the 10 random number
    """
    result = [i async for i in async_generator()]
    return result
