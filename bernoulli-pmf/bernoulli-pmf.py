import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x_vec = np.asarray(x, dtype=float)
    variance = p * (1.0 - p)

    pmf = np.asarray(np.where(x_vec==1, p, 1.0-p), dtype=float)

    return {
        "pmf": pmf,
        "mean": float(p),
        "variance": float(variance)
    }