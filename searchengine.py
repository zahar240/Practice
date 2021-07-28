text = input()
word = input()

def search(x, y):
    if x in y:
        return "Word found"
    else:
        return "Word not found"

print(search(text, word))