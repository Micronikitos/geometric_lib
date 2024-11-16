import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(calc("circle", "area", [5]), 78.5398, places=4)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(calc("circle", "perimeter", [5]), 31.4159, places=4)

    def test_square_area(self):
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_square_perimeter(self):
        self.assertEqual(calc("square", "perimeter", [4]), 16)

    def test_triangle_perimeter(self):
        self.assertEqual(calc("triangle", "perimeter", [3, 4, 5]), 12)

    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc("hexagon", "area", [5])

    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            calc("circle", "volume", [5])

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            calc("triangle", "area", [3, 4])
