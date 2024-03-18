#!/usr/bin/env python3
"""
4-tasks
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns task_wait_random n times with the specified max_delay
    Args:
        n(int): number of times to spawn wait_random
        max_delay(int): maximum delay for task_wait_random
    Return:
        a list of all the delays in ascending order
    """
    delays: list = []
    delay = [task_wait_random(max_delay) for i in range(n)]
    for s in asyncio.as_completed(delay):
        delays.append(await s)

    return delays
