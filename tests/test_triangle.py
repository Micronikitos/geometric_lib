import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_valid(self):
        self.assertEqual(area(3, 4, 5), 6.0) 

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 1, 10)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_valid(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_perimeter_zero_side(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)

if __name__ == "__main__":
    unittest.main()
