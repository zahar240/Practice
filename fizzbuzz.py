n = int(input())

def fizzbuzz_1():
    for x in range(1, n):
        if x%3 == 0 and x%5 == 0:
            print("SoloLearn")
        elif x%3 == 0 and x%2 == 1:
            print("Solo")
        elif x%5 == 0 and x%2 == 1:
            print("Learn")
        elif x%2 == 1:
            print(x)

def fizzbuzz_2():
    for x in range(1, n):
        s = '';
        if x % 3 == 0:
            s += 'Fizz'
        if x % 5 == 0:
            s += "Buzz"
        if s == '':
            s = x
    print(s, end=' ')

fizzbuzz_2()