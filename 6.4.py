# 6.4 Наследование классов (hard)
# Задание "Они все так похожи":

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = list(color)  # (список цветов в формате RGB)
        self.__sides = sides # (список сторон (целые числа))
        self.filled = False

    def get_color(self):   # возвращает список RGB цветов
        return self.__color



    def __is_valid_color(self, r, g, b):
        return all(0 <= i <= 255 for i in (r, g, b))



    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r,g,b


    def __is_valid_sides(self, *kwarg):
        return len(kwarg) == self.sides_count and all(isinstance(x, int) and x > 0 for x in kwarg)


    def get_sides(self):   # Стороны
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
       return self.__radius == self.__len__() / (2 * pi)

    def get_square(self):
       return (self.sides**2)/(4 * pi)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self.get_sides()) / 2   # Полу-периметр для формулы Герона
        return sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))




class Cube(Figure):
    sides_count = 12

    def __init__ (self, color, sides) :
        super().__init__(color, sides)
        self.sides = [sides] * self.sides_count

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # Цвет, стороны
cube1 = Cube((222, 35, 130), 6)

#Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  #
print(circle1.get_color())
cube1.set_color(300, 70, 15)  #
print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  #
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())

