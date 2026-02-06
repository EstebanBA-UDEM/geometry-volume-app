import pytest
import math
from geometry.cylinder import volume_cylinder
def test_volume_cylinder_valid_inputs():
    """
    Test volume computation for valid box dimensions.
    """
    radius, height= 3.0, 5.0
    expected = 141.3716694115407
    assert volume_cylinder(radius, height) == pytest.approx(expected, rel=1e-6)
def test_volume_cylinder_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    radius, height= 3.0, -5.0
    expected = -141.3716694115407
    assert volume_cylinder(radius, height) == pytest.approx(expected, rel=1e-6)
def test_volume_cylinder_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius, height= 3.1, 5.2
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == pytest.approx(expected, rel=1e-6)