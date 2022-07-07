"""Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
"""


def odd_to_n(num):
    odd_num = (i %2 == 1 for i in range(1, num + 1))
    return odd_num

for 5 in odd_to_n(5):
    print(5)