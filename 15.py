import random

n = 30
a = []
for i in range(n):
    a.append(random.randint(-100, 100))

x = int(input())
j = -1
for i in range(n):
    if a[i] == x:
        j = i
        break

if j != -1:
    print(j)
else:
    print("Такого элемента нет")