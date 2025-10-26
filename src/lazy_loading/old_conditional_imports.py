# Old way with imports inside functions to delay loading


def use_pandas():
    import pandas as pd

    return pd.DataFrame()  # Import happens here, repeated in every function


# Example usage
print(use_pandas())  # Loads pandas each time
