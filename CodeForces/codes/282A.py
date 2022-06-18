# Author: Abshar Mohammed Aslam, github.com/abxhr

n = int(input())
val = 0
lst = []
for i in range(n):
    q = input()[1]
    if '+' in q:
        val += 1
    else:
        val -= 1
print(val)
