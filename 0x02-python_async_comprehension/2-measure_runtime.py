#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension'
                                 ).async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using
        asyncio.gather and measure the total runtime
    Return:
        total runtime
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    total_time = time.perf_counter() - start

    return total_time
