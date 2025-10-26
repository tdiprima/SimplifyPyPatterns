# Old way using None as default and extra checks to handle unset values

from dataclasses import dataclass


@dataclass
class Settings:
    max_retries: int = None

    def __post_init__(self):
        if self.max_retries is None:
            self.max_retries = 5  # But can't distinguish explicit None


# Example usage
config = Settings()
print(config.max_retries)  # Outputs: 5
config_explicit = Settings(max_retries=None)
print(config_explicit.max_retries)  # Outputs: 5 (can't tell it was explicit)
