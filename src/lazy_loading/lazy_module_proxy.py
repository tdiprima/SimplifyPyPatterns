# Proxy for lazy-loading heavy modules on first attribute access

import importlib
import types


class DelayedModule(types.ModuleType):
    def __init__(self, module_name):
        super().__init__(module_name)
        self._module_name = module_name
        self._loaded_module = None

    def __getattr__(self, attr):
        if self._loaded_module is None:
            self._loaded_module = importlib.import_module(self._module_name)
        return getattr(self._loaded_module, attr)


# Expose lazy pandas as lpd
import sys

sys.modules["lpd"] = DelayedModule("pandas")

# Example usage: import lpd as pd  # Loads only on first use, e.g., pd.DataFrame
