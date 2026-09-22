import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # convert to numpy arrays
    vec_x = np.asarray(x, dtype=float)
    vec_y = np.asarray(y, dtype=float)

    # calculate dot product
    dot_prod = float(np.dot(vec_x, vec_y))

    return dot_prod