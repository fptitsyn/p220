import random

n = 40
a = []
for i in range(n):
    a.append(random.randint(-100, 100))

minim = 101

for i in a:
    if 0 < i < minim:
        minim = i

if minim < 101:
    print(minim)
else:
    print("Положительных нет")