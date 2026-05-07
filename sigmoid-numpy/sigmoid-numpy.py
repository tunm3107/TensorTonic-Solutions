import numpy as np
import math
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    def func(x):
        if x > 0:
            return 1 / (1 + math.e**(-x))
        else:
            return math.e**(x) / (1 + math.e**(x))
    vectorize_func = np.vectorize(func)
    return vectorize_func(x)