# В виде списка получить все возможные варианты порядка

from itertools import permutations

items = ["x", "y"]

print(list(permutations(items)))