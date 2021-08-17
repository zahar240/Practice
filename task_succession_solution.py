# Дополните предоставленный код для наследования класса Car от класса Vehicle
# Создайте объект класса Car и вызовите его метод horn(), который унаследован у класса-родителя Vehicle

class Vehicle:
    def horn(self):
        print("Beep!")

class Car(Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color

obj = Car("BMV","red")
obj.horn()