import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    cdf = 0
    for i in range(k+1):
        binomial_coefficient = math.comb(n, i)
        pmf = binomial_coefficient * (p**i) * (1 - p)**(n - i)
        cdf += pmf

    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }