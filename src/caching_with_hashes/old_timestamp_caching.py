# Old way using file timestamps for cache invalidation

import functools
import os
import time
from pathlib import Path


def memoize_with_timestamps(target_func):
    cache_dict = {}

    @functools.wraps(target_func)
    def wrapped(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            cached_time, result = cache_dict[key]
            if all(
                os.path.getmtime(arg) <= cached_time
                for arg in args
                if isinstance(arg, str) and Path(arg).exists
            ):
                return result
        result = target_func(*args, **kwargs)
        cache_dict[key] = (time.time(), result)
        return result

    return wrapped


# Example usage
@memoize_with_timestamps
def process_file(file_path):
    with open(file_path, "r") as f:
        return f.read().upper()


print(process_file("example.txt"))  # Invalidates on timestamp change
