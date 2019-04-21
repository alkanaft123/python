# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt as sqrt


class Triangle:
    A: tuple
    B: tuple
    C: tuple

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def get_lenght_side(self, dot1, dot2):
        return sqrt((dot1[0] - dot2[0]) ** 2
                    + (dot1[1] - dot2[1]) ** 2)

    def get_area(self):
        half_prmtr = self.get_perimeter() / 2

        return sqrt(half_prmtr *
                    (half_prmtr - self.get_lenght_side(self.A, self.B)) * (
                            half_prmtr - self.get_lenght_side(self.B, self.C)) * (
                            half_prmtr - self.get_lenght_side(self.A, self.C)))

    def get_perimeter(self):
        return self.get_lenght_side(self.A, self.B) + self.get_lenght_side(self.B, self.C) + self.get_lenght_side(
            self.A, self.C)

    # Вычисляем высоту треугольника
    def get_height(self):
        return (self.get_area() * 2) / self.get_lenght_side(self.A, self.B)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    A: tuple
    B: tuple
    C: tuple
    D: tuple
    triangle_1: Triangle
    triangle_2: Triangle

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.triangle_1 = Triangle(A, B, C)
        self.triangle_2 = Triangle(C, D, A)
        if self.get_lenght_side(A, C) == self.get_lenght_side(B, D):
            print('Trapeze is isosceles')
        else:
            print('Trapeze is NOT isosceles')

    def get_lenght_side(self, dot1, dot2):
        return sqrt((dot1[0] - dot2[0]) ** 2
                    + (dot1[1] - dot2[1]) ** 2)

    def get_perimeter(self):
        return self.get_lenght_side(self.A, self.B) + self.get_lenght_side(
            self.B, self.C) + self.get_lenght_side(
            self.A, self.C) + self.get_lenght_side(self.D, self.A)

    def get_area(self):
        return self.triangle_1.get_area() + self.triangle_2.get_area()


if __name__ == '__main__':
    triangle = Triangle((0, 0), (1, 1), (-1, 2))
    print(triangle.get_area())
    print(triangle.get_height())
    print(triangle.get_perimeter())

    trapeze_1 = Trapeze((0, 0), (1, 1), (3, 1), (4, 0))
    print(trapeze_1.get_area())
    print(trapeze_1.get_perimeter())
