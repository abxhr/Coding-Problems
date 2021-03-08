# Author: Abshar Mohammed Aslam, github.com/abxhr

n, h = map(int, input().split())
lst = list(map(int, input().split()))
rw = 0
for i in lst:
    if i > h:
        rw += 2
    else:
        rw += 1
print(rw)