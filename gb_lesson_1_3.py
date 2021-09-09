"""Реализовать склонение слова «процент» во фразе «N процентов». 
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

for number in range(1, 101):
    if number %10 == 1 and not number == 11:
       declension_word_percent = "процент"
    elif (number %10 == 2 or number %10 == 3 or number %10 == 4) and number != 12 and number != 13 and number != 14:
        declension_word_percent = "процента"
    else:
       declension_word_percent = "процентов"
    print(f"{number} {declension_word_percent}")