import random

n = 50
a = []
for i in range(n):
    a.append(random.randint(-100, 100))
j = -1
for i in range(n):
    if a[i] < 0:
        j = i
        break

if j > -1:
    print(j)
else:
    print("Отрицательных нет")