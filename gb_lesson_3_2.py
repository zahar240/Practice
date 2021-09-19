"""Доработать предыдущую функцию в num_translate_adv(): 
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. 
Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два" """


def num_translate_adv(english, dictionary):
    if english.istitle() :
        result = dictionary.get(english.lower())
        return result.capitalize()
    else:
        return dictionary.get(english)
        
          

english_russia = {
        "zero":"ноль",
        "one":"один",
        "two":"два",
        "three":"три",
        "four":"четыре",
        "five":"пять",
        "six":"шесть",
        "seven":"семь",
        "eight":"восемь",
        "nine":"девять",
        "ten":"десять"
        }

english_word = input("Enter a number in English from 0 to 10: ")

print(num_translate_adv(english_word, english_russia))