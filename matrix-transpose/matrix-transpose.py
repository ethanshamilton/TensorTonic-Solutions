import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # create rows
    transposed = [[] for i in range(len(A[0]))]
    
    # matrix transpose
    for i in range(len(A)):
        for j in range(len(A[i])):
            transposed[j].append(A[i][j])

    return np.asarray(transposed)