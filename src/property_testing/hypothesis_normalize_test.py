# Property-based test for a string normalization function using Hypothesis
# Run with: uv run pytest hypothesis_normalize_test.py -v

from hypothesis import given
from hypothesis import strategies as st


def format_text(input_str: str) -> str:
    return " ".join(word.title() for word in input_str.split())


@given(st.text())
def test_format_text(value):
    result = format_text(value)
    assert isinstance(result, str)
    assert result == result.strip()  # Additional property
