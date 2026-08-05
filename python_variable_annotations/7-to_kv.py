#!/usr/bin/env python3
from typing import Tuple, Union
"""Module to convert k into str and v into int or float """

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return key-value pair with v squared if it's a float."""
    if isinstance(v, float):
        return k, v ** 2
    return k, v
