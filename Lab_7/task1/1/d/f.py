n = int(input())
a = [int(i) for i in input().split()]

flag = False

for i in range(1, n - 1):
    if (a[i - 1] < a[i] and a[i] > a[i + 1]):
        flag = True
        break


if (flag):
    print("YES")
else:
    print("NO")