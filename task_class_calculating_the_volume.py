# Имеется класс Rectangle. 
# Создайте программу, которая получит два целых числа в качестве ввода,назначит одно за длинну, 
# а другое за ширину объекта и выведет площадь полученного прямоугольника


class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def vol(self):
        x = w * h
        print(x)

w = int(input())
h = int(input())

obj = Rectangle(w, h)
obj.vol()