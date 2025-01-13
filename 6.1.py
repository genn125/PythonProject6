# 6.1 "Зачем нужно наследование"
# Задача "Съедобное, несъедобное":

class Animal:

    def __init__(self, name):
        self.name=name
        self.fed = False                      # накормленный (нет)
        self.alive = True                     # живой

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True                    # накормленный (да)

        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False                  # живой (нет)

class Mammal(Animal):
    pass
class Predator(Animal):
    pass

class Plant:

    edible = False                               # съедобность (нет)
    def __init__(self, name):
        self.name=name

class Flower(Plant):
    pass
class Fruit(Plant):

    def __init__(self, name):
        Plant.__init__ (self, name)
        self.edible = True                          # съедобность (да), переопределение атрибута

a1 = Predator('Мой хищник')
a2 = Mammal('Чебурашка')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)








