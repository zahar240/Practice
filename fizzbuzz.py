n = input()

for x in range(1, n):
    if x%3 == 0 and x%5 == 0:
        print("SoloLearn")
    elif x%3 == 0 and x%2 == 1:
        print("Solo")
    elif x%5 == 0 and x%2 == 1:
        print("Learn")
    elif x%2 == 1:
        print(x)