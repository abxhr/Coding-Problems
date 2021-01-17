# Author: Abshar Mohammed Aslam, github.com/abxhr

n = int(input())
p = list(map(int, input().split()))[1:]
q = list(map(int, input().split()))[1:]
all = set(p+q)
f = 0
for i in range(1,n+1):
    if i not in all:
        f = 1
        break
if f == 0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")