# Author: Abshar Mohammed Aslam, github.com/abxhr

str = set(input().strip('{}').split(', '))
c = 0
for i in str:
    if i.isalpha():
        c += 1
print(c)
