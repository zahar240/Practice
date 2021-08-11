text = input("Введите текст: ")

def uppercase_decorator(func):
    def wrapper(text):
        text = text.upper()
    return wrapper

@uppercase_decorator
def display_text(text):
    return(text)

print(display_text(text))    