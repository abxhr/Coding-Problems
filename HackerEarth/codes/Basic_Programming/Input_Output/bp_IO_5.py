# Author: Abshar Mohammed Aslam, github.com/abxhr

for i in range(int(input())):
    s1 = input()
    a = list(s1)
    b = list(input())
    for i in s1:
        if (i in b) and (i in a):
            a.remove(i)
            b.remove(i)
    print(len(a)+len(b))
