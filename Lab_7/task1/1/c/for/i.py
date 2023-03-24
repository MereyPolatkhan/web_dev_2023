import math
a = int(input())
i = 1
c = 0
while i <= math.sqrt(a):
    if a % i == 0:
        c += 1
        if a // i != i:
            c += 1
    i += 1
print(c) 
