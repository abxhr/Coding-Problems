from itertools import permutations
str, n = input().split()
n = int(n)
lst = list(permutations(str, n))
lst.sort()
for i in lst:
    for j in i:
        print(j, end='')
    print("")
