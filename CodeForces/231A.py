# Author: Abshar Mohammed Aslam, github.com/abxhr

n = int(input())
c = 0
s = []
for i in range(n):
    a = input()
    s.append(a.split())
temp = 0
for i in s:
    for j in i:
        if int(j) == 1:
            temp += 1
    if temp > 1:
        c += 1
    temp = 0

print(c)
