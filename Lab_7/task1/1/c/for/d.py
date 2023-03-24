x = input() 
d = int(input())

cnt = 0

for char in x:
    if d == int(char):
        cnt += 1

print(cnt)