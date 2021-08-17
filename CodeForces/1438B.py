# Author: Abshar Mohammed Aslam, github.com/abxhr

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for i in range(len(lst)):
        nlst = lst[:i]
        f = 0
        for j in nlst:
            if j == lst[i]:
                print("YES")
                f = 1
                break
        if f:
            break
    if f != 1:
        print("NO")
