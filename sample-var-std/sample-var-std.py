import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    np_x = np.asarray(x, dtype=float)
    mean = np.mean(np_x)
    ssd = 0

    for i in range(len(x)):
        ssd += (x[i] - mean) ** 2

    variance = ssd / (len(x) - 1)

    standard_deviation = np.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }