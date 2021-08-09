birth_years = [1995, 2004, 2019, 1988, 1977, 1902]

def old_2050(x):
    return 2050 - x

result = list(map(old_2050, birth_years))
print(result)

def old_2050_result():
    result = list(map(old_2050, birth_years))
    print(result)

old_2050_result()