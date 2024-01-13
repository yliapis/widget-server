"""
THIS IS AN TEST FILE FORTO SERVE AS A DEMONSTRATION

Feel free to delete this file if not needed
"""

from widget_server.noise import generate_uniform_noise


def test_generate_uniform_noise():
    """
    Test the generate_uniform_noise function
    """

    samples = 10_000
    radius = 1.0
    noise = generate_uniform_noise(samples, radius)

    assert len(noise) == samples

    assert -radius <= min(noise)
    assert radius >= max(noise)
    assert -radius <= sum(noise) / samples <= radius
