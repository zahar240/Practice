names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

print(list(filter(lambda x: len(x) > 5, names)))

def filter_names():
   print(list(filter(lambda x: len(x) >= 5, names)))

filter_names() 