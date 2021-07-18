weight = int(input())
height = float(input())
imt = weight / height ** 2
if imt < 18.5:
    print("Underweight")
    print(imt)
elif 18.5 <= imt < 25:
    print("Normal")
    print(imt)
elif 25 <= imt <30:
    print("Overweight")
    print(imt)
elif 30 <= imt:
    print("Obesity")
    print(imt) 