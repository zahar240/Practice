# Определен класс Cat, у которого два атрибута: color, legs
# Класс используется для создания 3х отдельных объектов, принадлежащих этому классу
# Метод init принимает два аргумента и присваивает их объекту в качестве его атрибутов
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# Экземпляры класса берут атрибуты - фрагменты связанных с ними данных
# В примере, экземпяры класса Cat имеют атрибуты color и legs
# Их можно получить, указав точку и имя аирибута после экземпляра
print(felix.color)
print(felix.legs)

class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

# Классы могут также иметь атрибуты класса, которые создаются путем присвоения переменных в теле класса
# На них можно ссылаться либо из экземпляров класса, либо с тела самого класса
# атрибуты класса общие для всех экземпляров класса
print(fido.legs)
print(Dog.legs)

# Попытка вызова атрибута экземпляра, который не был определен вызывает AttributeError 
# Такая же ошибка выдается при попытке вызова несуществующего метода
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
print(rect.color)