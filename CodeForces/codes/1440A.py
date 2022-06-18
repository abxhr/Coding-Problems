# Author: Abshar Mohammed Aslam, github.com/abxhr

t = int(input())


def Total(lst, a, b):
    total = 0
    for i in lst:
        if i == '0':
            total += a
        else:
            total += b
    return total


for i in range(t):
    n, c0, c1, h = map(int, input().split())
    s = list(input())
    large = 0
    small = 0
    total = Total(s, c0, c1)
    changes = 0
    if c0 > c1:
        large = '0'
        small = '1'
    elif c1 > c0:
        large = '1'
        small = '0'
    else:
        print(Total(s, c0, c1))
        continue

    for i in s:
        if i == large:
            s[s.index(large)] = small
            if total > Total(s, c0, c1) + h + (changes*h):
                changes += 1
                total = Total(s, c0, c1) + (changes*h)
            else:
                s[s.index(small)] = large
    print(total)
