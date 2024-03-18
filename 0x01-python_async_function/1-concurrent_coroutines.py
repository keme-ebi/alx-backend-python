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
    for i in range(n):
        delays.append(await wait_random(max_delay))

    delays = sorted(delays)

    return delays


def sorted(li: List[float]) -> List[float]:
    """
    sorts a list in ascending order
    Args:
        li(list(floats)): a list of floats
    Return:
        list of sorted floats
    """
    n: int = len(li)
    for i in range(n):
        for j in range(0, n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li
