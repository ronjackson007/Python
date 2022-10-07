arr = [1, 3, 5, 7, 2]
arr.sort()

for i in (arr):
    for j in range(0, i):
        j += i
        print(j)
