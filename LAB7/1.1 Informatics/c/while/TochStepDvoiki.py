n = int(input())
x = 1

while n >= x:
    if x == n:
        print("YES")
        break
    x *= 2
else: print("NO")