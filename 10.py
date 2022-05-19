import random

n = 20
a = []
for i in range(n):
    a.append(random.randint(0, 1000))
minim = 1001
for i in range (n):
    if a[i] % 2 != 0 and a[i] % 3 == 0 and a[i] < minim:
        minim = a[i]

print(minim)