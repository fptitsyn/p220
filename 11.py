import random

n = 30
a = []
for i in range(n):
    a.append(random.randint(-100, 100))
m = 0
s = 0
for i in range(n):
    if a[i] >= 0:
        s += a[i]
    else:
        m += 1

if m == 0:
    print("Отрицательных нет")

print(s)