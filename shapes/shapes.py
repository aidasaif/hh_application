from abc import abstractmethod, ABC
from math import pi, sqrt

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def name(self):
        return self.__class__.__name__


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть больше 0.')
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def name(self):
        return 'Круг'

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Треугольник не может существовать.')
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    def is_right_traingle(self):
        # ищем гипотенузу (== самая длинная сторона)
        sides = sorted([self.a, self.b, self.c])
        # в случае, если стороны выбраны вещественными числами, учитываем погрешность 1e-9
        # если числа целые - sides[2]**2 == sides[0]**2 + sides[1]**2
        is_right = abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-9
        return is_right

    def name(self):
        return 'Треугольник'


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def name(self):
        return 'Квадрат'



