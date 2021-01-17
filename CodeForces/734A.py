# Author: Abshar Mohammed Aslam, github.com/abxhr

n = int(input())
d = 0
a = 0
s = input()
for i in list(s):
    if i == "A":
        a += 1
    else:
        d += 1
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else: 
    print("Friendship")