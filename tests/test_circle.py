import unittest
import calculate


class TestCircle(unittest.TestCase):
    """
    area test
    """

    def test_zero_area_circle(self):
        res = calculate.calc("circle", "area", [0])
        self.assertEqual(res, 0)

    def test_simple_area_circle(self):
        res = calculate.calc("circle", "area", [6])
        self.assertEqual(res, 113.09733552923255)

    def test_negative_area_circle(self):
        res = calculate.calc("circle", "area", [-3])
        self.assertEqual(res, "arguments must be positive")

    def test_string_area_circle(self):
        res = calculate.calc("circle", "area", ["6"])
        self.assertEqual(res, "arguments must be integer")

    """
    perimeter test
    """

    def test_zero_perimeter_circle(self):
        res = calculate.calc("circle", "perimeter", [0])
        self.assertEqual(res, 0)

    def test_simple_perimeter_circle(self):
        res = calculate.calc("circle", "perimeter", [6])
        self.assertEqual(res, 37.69911184307752)

    def test_negative_perimeter_circle(self):
        res = calculate.calc("circle", "perimeter", [-3])
        self.assertEqual(res, "arguments must be positive")

    def test_string_perimeter_circle(self):
        res = calculate.calc("circle", "perimeter", ["6"])
        self.assertEqual(res, "arguments must be integer")
