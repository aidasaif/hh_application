from math import pi
from shapes.shapes import Circle, Triangle, Square
import unittest

class TestShapes(unittest.TestCase):

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)

    def test_circle_area(self):
        circle = Circle(1)
        return self.assertAlmostEqual(circle.area(), pi)

    def test_circle_name(self):
        c = Circle(5)
        self.assertEqual(c.name(), "Круг")

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        return self.assertAlmostEqual(triangle.area(), 6)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        return self.assertTrue(triangle.is_right_traingle())

    def test_triangle_name(self):
        c = Triangle(3, 4, 5)
        self.assertEqual(c.name(), "Треугольник")

    def test_square_area(self):
        square = Square(2)
        return self.assertAlmostEqual(square.area(), 4)

    def test_square_name(self):
        c = Square(5)
        self.assertEqual(c.name(), "Квадрат")


if __name__ == '__main__':
    unittest.main()
