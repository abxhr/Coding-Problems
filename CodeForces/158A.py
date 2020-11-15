lst = list(map(int, input().split()))
n = lst[0] 
k = lst[1] - 1
c = 0
lst = list(map(int, input().split()))
lst.sort(reverse = True)
for i in range(len(lst)):
    if lst[i] != 0:
        if lst[i] >= lst[k]:
            c += 1
print(c)