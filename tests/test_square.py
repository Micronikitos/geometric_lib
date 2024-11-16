import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(2), 4)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2), 8)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-2)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area([5])
