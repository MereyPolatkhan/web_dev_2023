n = int(input())
a = [int(i) for i in input().split()]

a = a[::-1]

for i in a:
    print(i, end=" ")