# Функция super - полезная функция наследования, которая указывает на родительский класс
# Предназначенна для поиска метода по его имени в суперклассе объекта

class A:
    def spam(self):
        print(1)

# super().spam()
class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()