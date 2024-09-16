class Animal:
    alive = True  # атрибут родительского класса (живай)
    fed = False  # атрибут родительского класса (накормленный)

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food,
                      Plant):  # Проверка является ли объект(1 аргумент) экземпляром или подклассом класса (2 аргумент)
            if food.edible:  # Если параметр food съедобный
                print(f'{self.name} съел {food.name}.')
                self.fed = True  # поменять на True(накормлен)
            else:
                print(f'{self.name} не стал есть {food.name}.')
                self.alive = False  # поменять на False(не живой)


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False  # # атрибут родительского класса (съедобность)

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        # Функция super позволяет не явно ссылаться на суперкласс. Ссылаясь не нужно явно писать имя суперкласса.
        self.edible = True


a1 = Predator('Змей Горыныч')
a2 = Mammal('Зайка серенький')
p1 = Flower('Аленькай цвяточек')
p2 = Fruit('Яблочко наливное')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
