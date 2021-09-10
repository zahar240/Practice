"""Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. 
Внимание: использовать только арифметические операции!
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
c) * Решить задачу под пунктом b, не создавая новый список.

17485588610
15392909930
"""

list_cube = []
list_cube_multiple_7 = []
sum_number_cube_multiple_7 = 0

for number in range(1, 101):
    if number %2 == 1:
        list_cube.append(number ** 3)

for number_cube in list_cube:
    sum_sing_number = 0
    while number_cube > 0:
        sum_sing_number = sum_sing_number + (number_cube %10)
        number_cube = number_cube // 10
    
   


print(list_cube)
print(list_cube_multiple_7)
print(sum_number_cube_multiple_7)
