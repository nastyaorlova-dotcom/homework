
text = input("Введите числа через пробел: ")
items = text.split()
s = int(input("Введите степень: "))
r = []
for x in items:
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        n = int(x)
        r.append(n ** s)
    else:
        r.append(x * s)
print("Вывод:", end=" ")
for y in r:
    print(y, end=" ")
