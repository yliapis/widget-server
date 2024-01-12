"""
THIS IS A TEST MODULE FILE FOR NOISE GENERATION TO SERVE AS A DEMONSTRATION

Feel free to delete this file if not needed
"""

import numpy as np


def generate_uniform_noise(samples: int, radius: float=1.0) -> np.ndarray:
    """
    Generates a uniform zero mean noise vector of length samples

    -1 <= nu_i <= 1
    """
    return (np.random.rand(samples) * 2 - 1) * radius
