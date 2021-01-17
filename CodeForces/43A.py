# Author: Abshar Mohammed Aslam, github.com/abxhr

n = int(input())
s = []
for i in range(n):
    s.append(input())
teams = list(set(s))
a, b = 0, 0
for i in s:
    if i == teams[0]:
        a += 1
    else:
        b += 1
if a > b:
    print(teams[0])
else:
    print(teams[1])