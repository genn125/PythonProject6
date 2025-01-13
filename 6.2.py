# 6.2 "Доступ к свойствам родителя. Переопределение свойств"
# Задача "Изменять нельзя получать"

class Vehicle:

    __COLOR_VARIANTS = ['красный', 'жёлтый', 'зеленый', 'белый']

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
         self.owner = owner             # владелец транспорта
         self.__model = __model            # модель (марка) транспорта
         self.__engine_power = __engine_power  # мощность двигателя
         self.__color = __color                 # название цвета
# 1
    def get_model (self):
        return f'Модель: {self.__model}'
# 2
    def get_horsepower (self):
        return f'Мощность двигателя: {self.__engine_power}'
# 3
    def get_color (self):
        return f'Цвет: {self.__color}'
# 4
    def print_info (self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')
# 5
    def set_color (self, new_color :str):
        if new_color.lower() in (__color.lower() for __color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Фёдор', 'Toyota Mark II', 'Красный', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. Вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('ЖЁЛТЫЙ')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
