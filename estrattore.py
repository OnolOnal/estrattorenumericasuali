import random

a = int(input("Min: "))
b = int(input("Max: "))
print("Num da escludere (e finire con N): ")
c = []
while True:
    d = input()
    if d == "N":
        break
    else:
        c.append(int(d))
f = int(input("Count: "))

e = []
while e.__len__() < f:
    g = random.randint(a, b)
    while g in c:
        g = random.randint(a, b)
    if e.__contains__(g) == False:
        e.append(g)
print(e)
