import random

n = 40
a = []
for i in range(n):
    a.append(random.randint(-100, 100))

l = 0
lmax = 0
for i in range(n):
    if i < n - 1:
        if a[i] < a[i+1]:
            l += a[i] + a[i+1]
        else:
            if l > lmax:
                lmax = l
            l = 0

print(lmax)
print(a)