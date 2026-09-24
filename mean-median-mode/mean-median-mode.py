from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    frequencies = Counter(x)
    mode = max(frequencies, key=lambda k: (frequencies[k], -k))
    
    np_x = np.asarray(x, dtype=float)
    
    return {
        "mean": float(np.mean(np_x)),
        "median": float(np.median(np_x)),
        "mode": float(mode)
    }