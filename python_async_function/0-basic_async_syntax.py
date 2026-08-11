#!/usr/bin/env python3
"""This module provides an async coroutine that waits
for a random delay before returning it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of time and return the delay"""
  
    random_number = random.uniform(0, max_delay)

    await asyncio.sleep(random_number)

    return random_number

