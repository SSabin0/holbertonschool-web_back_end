#!/usr/bin/env python3
"""Module for async generator that yields random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random numbers asynchronously."""
    for i in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
