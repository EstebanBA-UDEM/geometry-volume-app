import pytest
import math
from geometry.sphere import volume_sphere
def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid box dimensions.
    """
    radius= 3.0
    expected = 113.09733552923255
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius= 3.1
    expected = (4 / 3) * math.pi * radius ** 3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)