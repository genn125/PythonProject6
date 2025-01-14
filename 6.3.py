# Множественное наследование
# Задача "Ошибка эволюции

from random import randint as ran
#1
class Animal:
    _DEGREE_OF_DANGER = 0        # степень опасности существа
    live = True
    sound = None                 # звук (изначально отсутствует)
    _cords = [0, 0, 0]           #  координаты в пространстве
    def __init__(self, speed):
        self.speed = speed  # скорость передвижения существа
#1,1
    def move(self, dx, dy, dz):    # Движение
        self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]
        if self._cords[2] < 0:
            pass
        else:
            print("5 >    It's too deep, i can't dive :(  # Здесь слишком глубоко, я не могу нырнуть")
#1,2
    def get_cords(self):  # координаты
        print(f'6(7) > X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
#1,3
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("4 >    Sorry, i'm peaceful :)")        # Извините, я настроен миролюбиво
        else:
            print("4 >    Be careful, i'm attacking you 0_0")       # Будь осторожен, я атакую тебя
#1,4
    def speak(self):       # выводит строку со звуком sound
        print(self.sound)
#2
class Bird (Animal):
    beak = True                      # наличие клюва

    def lay_eggs(self):
        print(f'8 >    Here are(is) {ran(1, 4)} eggs for you')
#3
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3            # степень опасности существа

    def dive_in(self, dz):           # погружение
        self._cords[2] -= self.speed * dz // 2
#4
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8               # степень опасности существа
#5
class Duckbill(PoisonousAnimal, AquaticAnimal,Bird ):
    sound = "3 >    Click-click-click"

db = Duckbill(10)

print(f'1 >    {db.live}')
print(f'2 >    {db.beak}')

db.speak()
db.attack()

db.move(1, 2, 3)   # Движение

db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()


