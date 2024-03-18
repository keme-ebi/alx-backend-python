#!/usr/bin/env python3
"""
1-concurrent_coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with the specified max_delay
    Args:
        n(int): number of times to spawn wait_random
        max_delay(int): maximum delay for wait_random
    Return:
        a list of all the delays in ascending order
    """
    delays: list = []
    delay = [wait_random(max_delay) for i in range(n)]
    for s in asyncio.as_completed(delay):
        delays.append(await s)

    return delays
