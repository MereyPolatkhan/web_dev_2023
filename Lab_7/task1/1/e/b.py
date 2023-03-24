def func(a, b):
    res = 1.0
    for i in range(1, b + 1):
        res *= a
    return res

a = input().split()
print(func(float(a[0]), int(a[1])))