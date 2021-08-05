file = open("books.txt", encoding="utf-8")
file_2 = open(r"C:\Users\Дом\Desktop\python\auxiliary_materials\books.txt", encoding="utf-8")
#print(file.read())
#print(file_2.read())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readlines())

def row_file():
    for i in file:
        print(i)

def letter_file():
    for i in file:
        for y in i:
            print(y)

def booktitles_1():
    for i in file:
        print(i[0] + str(len(i)))

def booktitles_2():
    s = file.readlines()

    print(s)



#row_file()
#letter_file()
#booktitles_1()
booktitles_2()

file.close()
file_2.close()
