# Atomic file writing to avoid partial writes using temp files and replace

import os
import tempfile

from icecream import ic


def safe_write_file(file_path, content, write_mode="w"):
    # Determine the directory of the target file
    directory = os.path.dirname(file_path) or "."
    ic(directory)

    # Create a temporary file in the same directory
    file_desc, temp_path = tempfile.mkstemp(dir=directory)
    ic(file_desc, temp_path)

    # Write content to the temporary file
    with os.fdopen(file_desc, write_mode) as file_handle:
        file_handle.write(content)
    
    # Atomically replace the target file with the temporary file
    os.replace(temp_path, file_path)


# Example usage
safe_write_file("example.txt", "Hello, world!")
