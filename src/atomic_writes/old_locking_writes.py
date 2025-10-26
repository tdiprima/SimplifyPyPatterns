# Old way using file locking to prevent concurrent issues

import fcntl


def write_with_lock(file_path, content):
    with open(file_path, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)  # Acquire lock
        f.write(content)
        fcntl.flock(f, fcntl.LOCK_UN)  # Release lock


# Example usage
write_with_lock("example.txt", "Hello, world!")
