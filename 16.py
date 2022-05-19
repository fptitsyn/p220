import random

n = 40
a = []
for i in range(n):
    a.append(random.randint(-100, 100))

max = 0
k = 0
for i in range(n):
    if a[i] > max:
        max = a[i]

k = max
max = 0

for i in range(n):
    if max < a[i] < k:
        max = a[i]

print(max)
