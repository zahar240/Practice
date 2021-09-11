"""Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. 
Внимание: использовать только арифметические операции!
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
c) * Решить задачу под пунктом b, не создавая новый список.

17485588610
15392909930
"""

cube = []
cube_plus_17 = []
sum_multiple_7 = 0
sum_multiple_7_plus_17 = 0


for number in range(1, 1001, 2):
    cube.append(number ** 3)
    cube_plus_17.append(number ** 3 + 17)

for number in cube:
    digit_sum = 0
    number_7 = number
    while number > 0:
        digit_sum += number %10
        number //= 10
    if digit_sum %7 == 0:
        sum_multiple_7 += number_7

for number in cube_plus_17:
    digit_sum = 0
    number_7 = number
    while number > 0:
        digit_sum += number %10
        number //= 10
    if digit_sum %7 == 0:
        sum_multiple_7_plus_17 += number_7


print(sum_multiple_7)
print(sum_multiple_7_plus_17)
