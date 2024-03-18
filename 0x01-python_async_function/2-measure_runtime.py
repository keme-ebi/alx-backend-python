#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    Args:
        n(int): number of times wait_n spawns wait_random
        max_delay(int): maximum delay time for wait_random
    Return:
        total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return (total_time / n)
