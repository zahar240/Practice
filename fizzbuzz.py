n = int(input())

def fizzbuzz_1():
    for x in range(1, n):
        if x % 3 == 0 and x % 5 == 0:
            print("SoloLearn")
        elif x % 3 == 0 and x % 2 == 1:
            print("Solo")
        elif x % 5 == 0 and x % 2 == 1:
            print("Learn")
        elif x % 2 == 1:
            print(x)

def fizzbuzz_2():
    i = 1
    while i <= n:
        if i % 2 == 1 and i % 3 == 0:
            print("Solo")
        elif i % 2 == 1 and i % 5 == 0:
            print("Learn")
        elif i % 3 == 0 and i % 5 == 0:
            print("SoloLearn")
        elif i % 2 == 1:
            print(i)
        i += 1
        

def fizzbuzz_3():

                
#fizzbuzz_1()
fizzbuzz_2()