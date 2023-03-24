x = int(input())
i = 2
while(i <= x):
    if not x % i:
        print(i)
        break

    i += 1