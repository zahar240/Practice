# Для модификации функций с помощью других фукций
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello words!")

decorated = decor(print_text)
decorated()

# print_text полностью заменяется декорированной версией путем повторного присвоения переменной, содержащей функцию
print_text = decor(print_text)
print_text()

# Если определяется функция, ее можно обернуть в декоратор поставив перед определением функции @ и имя декоратора
@decor
def print_text():
    print("Hello words!_2")

print_text()


