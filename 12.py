import random

n = 28
a = []
for i in range(n):
    a.append(random.randint(0, 100))
minim = 101
for i in a:
    if 40 < i < minim:
        minim = i

print(minim)