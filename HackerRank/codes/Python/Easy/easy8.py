n = int(input())
a = []

for i in (input().split()):
    a.append(int(i))

lst = [float("-inf"), float("-inf")]
for i in a:
    if i > lst[0]:
        lst[1] = lst[0]
        lst[0] = i
    elif i < lst[0]:
        if i > lst[1]:
            lst[1] = i

print(lst[1])
