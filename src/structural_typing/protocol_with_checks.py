# Defines a protocol for structural typing and runtime checks for plugins

from typing import Protocol, runtime_checkable


@runtime_checkable
class Logger(Protocol):
    def log(self, message: str) -> None: ...


def record(log_obj: Logger, message: str):
    from typeguard import check_type

    check_type(log_obj, Logger)  # Runtime check
    log_obj.log(message)


# Example usage
class SimpleLogger:
    def log(self, message: str) -> None:
        print(f"Logged: {message}")


record(SimpleLogger(), "Test message")
