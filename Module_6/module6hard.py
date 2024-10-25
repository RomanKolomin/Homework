from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color=(255, 255, 255), *sides):
        self.__color = list(color)
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b):
        return all(isinstance(number, int) and 0 <= number <= 255 for number in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figure__sides[0] / (2*pi)

    def get_square(self):
        return pi * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self._Figure__sides[0], self._Figure__sides[1], self._Figure__sides[2]
        return 0.25 * ((a+b-c)*(a-b+c)*(-a+b+c)*(a+b+c))**(1/2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._Figure__sides = list(sides * self.sides_count) if len(sides) == (1 or 12) else [1] * self.sides_count

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
