# Uses a sentinel object to distinguish between unset values and explicit None

_SENTINEL = object()

from dataclasses import dataclass


@dataclass
class Settings:
    max_retries: int = _SENTINEL

    def __post_init__(self):
        if self.max_retries is _SENTINEL:
            self.max_retries = 5  # Default value set clearly


# Example usage
config = Settings()
print(config.max_retries)  # Outputs: 5
config_explicit = Settings(max_retries=None)
print(config_explicit.max_retries)  # Outputs: None
