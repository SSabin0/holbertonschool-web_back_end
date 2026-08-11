#!/usr/bin/env python3
"""Module that runs multiple coroutines at the same time using tasks."""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with max_delay and return delays in ascending order."""
    coroutines = []
    for i in range(n):
        coroutines.append(task_wait_random(max_delay))

    results = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        results.append(result)

    return results
