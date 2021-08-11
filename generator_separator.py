txt = input()

def words():
    x = txt.split()
    for i in x:
        yield x
        i += x

print(list(words()))