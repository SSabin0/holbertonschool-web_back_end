#!/usr/bin/env python3
"""Module for measuring the total execution time of wait_n coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n and return time per coroutine."""
    start_time = time.perf_counter()
    results = asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    lapsed = end_time - start_time
    return lapsed / n
