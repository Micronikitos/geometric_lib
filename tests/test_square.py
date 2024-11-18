import unittest
import calculate


class TestSquare(unittest.TestCase):
    """
    area test
    """

    def test_zero_area_square(self):
        res = calculate.calc("square", "area", [0])
        self.assertEqual(res, 0)

    def test_simple_area_square(self):
        res = calculate.calc("square", "area", [6])
        self.assertEqual(res, 36)

    def test_negative_area_square(self):
        res = calculate.calc("square", "area", [-3])
        self.assertEqual(res, "arguments must be positive")

    def test_string_area_square(self):
        res = calculate.calc("square", "area", ["6"])
        self.assertEqual(res, "arguments must be integer")

    """
    perimeter test
    """

    def test_zero_perimeter_square(self):
        res = calculate.calc("square", "perimeter", [0])
        self.assertEqual(res, 0)

    def test_simple_perimeter_square(self):
        res = calculate.calc("square", "perimeter", [6])
        self.assertEqual(res, 24)

    def test_negative_perimeter_square(self):
        res = calculate.calc("square", "perimeter", [-3])
        self.assertEqual(res, "arguments must be positive")

    def test_string_perimeter_square(self):
        res = calculate.calc("square", "perimeter", ["6"])
        self.assertEqual(res, "arguments must be integer")
