# Author: Abshar Mohammed Aslam, github.com/abxhr

import sys

n, m = map(int, input().split())
c = []
bw = ['W', 'B', 'G']
for i in range(n):
    c.append(input().split())
for i in c:
    for j in i:
        if j not in bw:
            print("#Color")
            sys.exit(0)
print("#Black&White")
