# Composes small functions into a pipeline for data transformation

from functools import reduce


def build_pipeline(*functions):
    return lambda input_val: reduce(lambda val, func: func(val), functions, input_val)


def remove_whitespace(val):
    return val.strip()


def to_upper(val):
    return val.upper()


def single_space(val):
    return " ".join(val.split())


process = build_pipeline(remove_whitespace, to_upper, single_space)
print(process("  hello   world "))  # Outputs: "HELLO WORLD"
