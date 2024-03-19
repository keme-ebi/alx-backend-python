#!/usr/bin/env python3
"""
0-async_generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    loops 10 times, wait 1 second, then yield a random number between
        0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
