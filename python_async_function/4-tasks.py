#!/usr/bin/python3
"""Defines a new function task_wait_n"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    list_delays = [task_wait_random(max_delay) for i in range(n)]

    delays = []
    for delay in asyncio.as_completed(list_delays):
        delays.append(await delay)
    return delays
