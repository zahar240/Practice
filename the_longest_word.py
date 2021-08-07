#Using the text as input data, find and output the longest word in the result.

txt = input().split()

def longest_word():
    length_word = []
    for i in txt:
        length_word.append(len(i))
    print(txt[length_word.index(max(length_word))])

longest_word()
