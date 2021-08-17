# С помощью наследования мы можем задать единую функциональность разным классам
# Некоторые методы классов Cat и Dog уникальны: только у Cat метод purr, только у Dog метод bark
# Другие методы одинаковы для обоих классов: color и name, - это сходство можно выразить с помощью функции наследования
# Все классы наследуют общую функциональность от суперкласса Animal
# Наследование оформляется путем заключения в круглые скобки имени суперкласса, следующего за именем класса
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

# Класс, наследующий атрибуты или методы другого класса, называется подклассом
# Класс, из которого наследуются атрибуты или методы, называется суперклассом
# Wolf - суперкласс
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

# Если наследуемый класс имеет такие же атрибуты или методы, что и класс-наследник, то класс-наследник переопределяет их
# Dog - подкласс
class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()
