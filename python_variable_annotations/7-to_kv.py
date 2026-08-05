from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return key-value pair with v squared if it's a float."""
    if isinstance(v, float):
        return k, v ** 2
    return k, v

print(to_kv.__annotations__)
print(to_kv("eggs", 9))
print(to_kv("school", 0.02))
