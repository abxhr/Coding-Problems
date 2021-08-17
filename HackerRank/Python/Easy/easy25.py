from itertools import product
for i in product(list(map(int, input().split())), list(map(int, input().split()))):
    print(str(i), end=" ")
