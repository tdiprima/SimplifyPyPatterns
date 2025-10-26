# Old way using a loop or nested calls for transformations


def process_text(input_val):
    val = input_val.strip()
    val = val.upper()
    val = " ".join(val.split())
    return val


print(process_text("  hello   world "))  # Outputs: "HELLO WORLD"
