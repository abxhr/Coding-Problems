# Author: Abshar Mohammed Aslam, github.com/abxhr

k, n, w = map(int, input().split())
extra = 0
for i in range(1, w+1):
    if n >= k*i:
        n -= k*i
    elif n > 0:
        c = k*i - n
        n -= n
        extra += c
    else:
        extra += k*i
print(extra)
