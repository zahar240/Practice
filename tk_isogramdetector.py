# 1. Task
"""
An isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive.
Your job is to find a way to detect if a word is an isogram.

Task: Write a program that takes in a string as input, detects if the string is an isogram and outputs true or false based on the result.

Input Format:
A string containing one word.

Output Format:
A string: true or false.

Sample Input:
turbulence

Sample Output:
false
"""


# 2. Solution logic
"""
1. Прописать переменную, которая получает значение пользовательским вводом, тип данных - строка.
2. Преобразовать строку в список.
3. Прописать цикл, в котором каждый элемент списка будет сравниваться с его элементами на соответствие.
4. Прописатьусловие сравнения.
5. Вывести полученный результат.
"""


# 3. Solution

someword = list(input())
print(someword)

def isogramdetector():
   num = 1
   for i in someword:
      if i == someword.count(i):
         print("True_Folse")
         return num == someword.count(i)
      

isogramdetector()



   