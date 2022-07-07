"""Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration..."""


def odd_to_n(num):
    for i in range(1, num + 1):
        yield i


n = int(input("Введите число: "))

for n in odd_to_n(n):
    print(n)
print(next(odd_to_n(n)))
