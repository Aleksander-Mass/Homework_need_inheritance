'''
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут
alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
'''

#    Пункты задачи:

# 1. Создайте классы Animal и Plant с соответствующими атрибутами и методами

# 2. Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
#    При необходимости переопределите значения атрибутов.

# 3. Создайте объекты этих классов.



# Родительский класс для животных

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

# Родительский класс для растений
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

# Класс Млекопитающих (наследник Animal)
class Mammal(Animal):
    pass

# Класс Хищников (наследник Animal)
class Predator(Animal):
    pass

# Класс Цветов (наследник Plant)
class Flower(Plant):
    pass

# Класс Фруктов (наследник Plant)
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобны по умолчанию

# Создание объектов и проверка
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее съедает фрукт

print(a1.alive)  # Волк умер
print(a2.fed)  # Хатико сыт

# Вывод на консоль:
'''
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True
'''