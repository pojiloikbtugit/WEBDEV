a = []
res = 0
for i in range(int(input())):
    a.append(int(input())) 
for elem in range(len(a)):
    if a[elem] > a[elem - 1]:
        res += 1
print(res)
