text = input()
word = input()

def search(x, y):
    if word in text:
        return "Word found"
    else:
        return "Wrd not found"

print(search(text, word))