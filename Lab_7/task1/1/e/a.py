def func(a, b, c, d):
    return min(min(a, b), min(c, d))

a = input().split()
print(func(int(a[0]), int(a[1]), int(a[2]), int(a[3])))