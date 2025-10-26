# Old way with manual unit tests for specific cases
# pytest old_unit_tests.py -v

def format_text(input_str: str) -> str:
    return " ".join(word.title() for word in input_str.split())


def test_format_text():
    assert format_text("hello world") == "Hello World"
    assert format_text("") == ""
    assert format_text("   ") == ""
    # Limited to these cases, misses edges


# Run manually or with a test runner
test_format_text()
