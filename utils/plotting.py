from typing import Any, Callable
import numpy as np

@np.vectorize
def format_label(original: Any, fn: Callable):
    return fn(original)
