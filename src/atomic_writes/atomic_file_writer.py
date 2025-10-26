# Atomic file writing to avoid partial writes using temp files and replace

import os
import tempfile


def safe_write_file(file_path, content, write_mode="w"):
    directory = os.path.dirname(file_path) or "."
    file_desc, temp_path = tempfile.mkstemp(dir=directory)
    with os.fdopen(file_desc, write_mode) as file_handle:
        file_handle.write(content)
    os.replace(temp_path, file_path)


# Example usage
safe_write_file("example.txt", "Hello, world!")
