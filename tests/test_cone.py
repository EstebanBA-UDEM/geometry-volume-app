import pytest
import math
from geometry.cone import volume_cone
def test_volume_cone_valid_inputs():
    """
    Test volume computation for valid box dimensions.
    """
    base_radius, height= 3.0, 5.0
    expected = 47.12388980384689
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)
def test_volume_cone_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    base_radius, height= 3.0, -5.0
    expected = -47.12388980384689
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)
def test_volume_cone_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    base_radius, height= 3.1, 5.2
    expected = (1/3) * math.pi * base_radius**2 * height
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)