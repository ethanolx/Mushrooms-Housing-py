from typing import Any, Callable
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


@np.vectorize
def format_label(original: Any, fn: Callable):
    return fn(original)
