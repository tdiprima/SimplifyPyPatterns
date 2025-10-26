# Old way with manual attribute and type checks in functions


def record(log_obj, message: str):
    if not hasattr(log_obj, "log") or not callable(log_obj.log):
        raise ValueError("Object must have a callable 'log' method")
    log_obj.log(message)


# Example usage
class SimpleLogger:
    def log(self, message: str) -> None:
        print(f"Logged: {message}")


record(SimpleLogger(), "Test message")
