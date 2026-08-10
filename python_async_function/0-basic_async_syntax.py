import asyncio
import random
"""Create a module to generate a random wait time based on 0 to max delay number given"""


async def wait_random(max_delay: int = 10) -> float:
  """Wait for a random amount of time and return the delay"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
