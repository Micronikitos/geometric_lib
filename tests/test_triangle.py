import unittest
import calculate

class TestTriangle(unittest.TestCase):

    '''
    area test
    '''

    def test_zero_area_triangle(self):
        res = calculate.calc("triangle", "area", [0, 0, 0])
        self.assertEqual(res, 0)

    def test_simple_area_triangle(self):
        res = calculate.calc("triangle", "area", [2, 5, 6])
        self.assertEqual(res, 4.683748498798798)

    def test_negative_area_triangle(self):
        res = calculate.calc("triangle", "area", [-3, 2, -1])
        self.assertEqual(res, "arguments must be positive")

    def test_string_area_triangle(self):
        res = calculate.calc("triangle", "area", ["6", 2, "6"])
        self.assertEqual(res, "arguments must be integer")

    '''
    perimeter test
    '''

    def test_zero_perimeter_triangle(self):
        res = calculate.calc("triangle", "perimeter", [0, 0, 0])
        self.assertEqual(res, 0)

    def test_simple_perimeter_triangle(self):
        res = calculate.calc("triangle", "perimeter", [2, 5, 6])
        self.assertEqual(res, 13)

    def test_negative_perimeter_triangle(self):
        res = calculate.calc("triangle", "perimeter", [-3, 2, -1])
        self.assertEqual(res, "arguments must be positive")

    def test_string_perimeter_triangle(self):
        res = calculate.calc("triangle", "perimeter", ["6", 2, "6"])
        self.assertEqual(res, "arguments must be integer")