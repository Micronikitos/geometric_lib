import unittest
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(area(1), 3.14159, places=5)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(1), 6.28318, places=5)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter("radius")
