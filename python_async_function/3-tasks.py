#!/usr/bin/env python3
"""Module that creates an asyncio Task from wait_random coroutine."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Take an integer max_delay and return an asyncio Task."""
    task = asyncio.create_task(wait_random(max_delay))
    return task
