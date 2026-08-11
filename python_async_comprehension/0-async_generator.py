#!/usr/bin/env python3
"""Module for async generator that yields random numbers."""
import asyncio
import random


async def async_generator():
    """Module to asynchronously wait 1 second then yield a number between
    0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
