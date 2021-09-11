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
    elif number %10 in (2, 3, 4) and number not in (12, 13, 14):
        declension_word_percent = "процента"
    else:
       declension_word_percent = "процентов"
    print(f"{number} {declension_word_percent}")