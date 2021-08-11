def decor(func):
    def wrap():
        print("###")
        func()
        print("###")
    return wrap


def print_bill():
    print("BILL DATA GOES HERE")

print_bill = decor(print_bill)


@decor
def print_bill_2():
    print("Bill Data Goes Here")


print_bill()
print_bill_2()
