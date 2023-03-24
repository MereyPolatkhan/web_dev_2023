n = input()

n = n[::-1]

s = 0

for i in range(0, len(n)):
    if (n[i] == "1"):
        s += 2**(i)

print(s)