# Decorator for caching function results based on args and file content hashes

import functools
import hashlib
from pathlib import Path


def compute_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def memoize_with_hashes(target_func):
    cache_dict = {}

    @functools.wraps(target_func)
    def wrapped(*args, **kwargs):
        arg_hashes = tuple(
            compute_hash(arg) if isinstance(arg, str) and Path(arg).exists else arg
            for arg in args
        )
        cache_key = (arg_hashes, tuple(sorted(kwargs.items())))
        if cache_key in cache_dict:
            return cache_dict[cache_key]
        result = target_func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result

    return wrapped


# Example usage
@memoize_with_hashes
def process_file(file_path):
    with open(file_path, "r") as f:
        return f.read().upper()


print(process_file("example.txt"))  # Caches based on content hash
