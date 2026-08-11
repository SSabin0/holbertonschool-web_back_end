#!/usr/bin/env python3
"""Module for multiple coroutines at the same time"""

import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with given max_delay
    and return the delays in a list
    """

    coroutines = []
    for i in range(n):
        coroutines.append(wait_random(max_delay))

    results = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        results.append(result)

    return results
