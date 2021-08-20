# Выражение x = y представляется как x.__add__(y)
# Если метод __add__ не выполняется, а х и у различных типов, тогда используеся y.__radd__(x)

# У всех магических методах (__sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __and__,
# __xor__, __or__) есть аналогичные методы r

# В приведенном примере определена операция разделения для класса SpecalString

class SpecalString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecalString("spam")
hello = SpecalString("Hello world!")
print(spam / hello)