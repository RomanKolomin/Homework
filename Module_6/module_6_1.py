class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if Plant.return_edible(food):
            print(f'{self.name} съел {food}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food}')
            self.alive = False


class Plant:
    edible = False

    def return_edible(self):
        return self.edible

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
