# Модуль itertools

# count - создает бесконечную прогессию вверх от заданного числа
from itertools import count
# accumulate - возвращает сумму значений внутри итерируемого объекта
# takewhile - возвращает элементы из итерируемого объекта, которые удовлетворяют предикативной функции
from itertools import accumulate, takewhile
# product, permutations - используются, когда нужно выполнить задачу со всеми возможными коминациями некоторых элементов
from itertools import product, permutations

for i in count(3):
    print(i)
    if i >= 11:
        break

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

letters = ("A","B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
