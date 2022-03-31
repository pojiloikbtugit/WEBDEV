a = []
for i in range(int(input())):
    a.append(int(input())) 
for elem in range(len(a)):
    if elem % 2 == 0:
        print(a[elem])
