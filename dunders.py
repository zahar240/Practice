# Предназначены для создания специальной функциональности
# Часто применяются для переопределения операторов

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Метод __add__ позволяет определить специальное поведение  для оператора + в нашем классе
# Определяются соответствующие атрибуты объектов и возвращается новый объект, содержащий результат
# После можно объеденить два объекта класса
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)