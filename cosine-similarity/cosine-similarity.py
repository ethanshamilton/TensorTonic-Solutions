import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # convert inputs to numpy arrays
    vec_a = np.asarray(a, dtype=float)
    vec_b = np.asarray(b, dtype=float)

    # calculate numerator
    numerator = np.dot(vec_a, vec_b)

    # calculate denominator
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    denominator = norm_a * norm_b

    if norm_a == 0 or norm_b == 0:
        return float(0.0)

    return float(numerator/denominator)