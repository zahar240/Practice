"""Написать функцию thesaurus_adv(), 
принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
в котором ключи — первые буквы фамилий, а значения — словари, 
реализованные по схеме предыдущего задания и содержащие записи, 
в которых фамилия начинается с соответствующей буквы. 
Например:
>>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    }, 
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"], 
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?"""


from os import name


def thesaurus_adv(*names):
    names_dict = {}
    for name in sorted(names):
        n, s = name.split()
        val = names_dict.setdefault(s[0], {n[0]: name})
        n_val = val.setdefault(n[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_dict


def thesaurus_adv_2(*names):
    s_n_sort = {}
    for s_n in names:
        s_n.sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split[0][0], []).append(s_n)
    return s_n_sort


list_names = ("Qqqq Wwwww", "Aaaaa Ssssss", "Zzzz Xxxxxxx", "Eeeee Rrrrrr", "Tttt Uuuuuu",
"Cccc Bbbbb", "Nnnn Mmmmm", "Hhhh Kkkkkk", "Iiii Ooooo", "Pppp Gggggg")

print(thesaurus_adv(list_names))
print(thesaurus_adv_2(list_names))