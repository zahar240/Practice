# Один класс может наследовать от другого класса, который в свою очередь может наследовать от третьего класса
# Круговое наследование не поддерживаеся

class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_method()
c.third_method()
