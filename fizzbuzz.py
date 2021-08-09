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
    slbox = []
    for i in range(1, n):
        if i % 2 == 1 and i % 3 == 0 and i % 5 == 0:
            slbox.append("SoloLearn")
        elif i % 2 == 1 and i % 3 == 0:
            slbox.append("Solo")
        elif i % 2 == 1 and i % 5 == 0:
            slbox.append("Learn")
        elif i % 2 == 1:
            slbox.append(str(i))
    print(slbox)

def fizzbuzz_4():
    slbox = []
    for i in range(1, n):
        slbox.append("SoloLearn") if i % 2 == 1 and i % 3 == 0 and i % 5 == 0 else None
        slbox.append("Solo") if i % 2 == 1 and i % 3 == 0 else None
        slbox.append("Learn") if i % 2 == 1 and i % 5 == 0 else None
        slbox.append(str(i)) if i % 2 == 1 else None
    print(slbox)

def fizzbuzz_5():
    for i in range(1, n):
        s = " "
        if i % 2 == 1 and i % 3 == 0:
            s += "Solo"
        if i % 2 == 1 and i % 5 == 0:
            s += "Learn"
        if i % 2 == 1 and i % 3 !=0 and i % 5 != 0:
            s += str(i)
        print(s)

def fizzbuzz_6():
    for i in range(1, n):
        s = ''
        if i % 2 == 1 and i % 3 == 0:
            s += 'Solo'
        if i % 2 == 1 and i % 5 == 0:
            s += "Learn"
        if i % 2 == 1 and s == '':
            s = i
        print(s)
    
#fizzbuzz_1()
#fizzbuzz_2()
#fizzbuzz_3()
#fizzbuzz_4()
#fizzbuzz_5()
fizzbuzz_6()