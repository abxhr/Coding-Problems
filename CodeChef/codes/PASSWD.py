# Author: Abshar Mohammed Aslam, github.com/abxhr

t = int(input())
small = list("abcdefghijklmnopqrstuvwxyz")
cap = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dig = list("0123456789")
spec = ['@', '#', '%', '&', '?']
while(t):
    t -= 1
    s = input()
    p = 0
    if not(len(s) >= 10):
        print("NO")
        continue
    else:
        p += 1

    first_c = True
    second_c = True
    third_c = True
    fourth_c = True

    for i in range(len(s)):
        c = s[i]
        if (c in small) and (first_c):
            p += 1
            first_c = False

        if (c in cap) and (second_c) and ((i != 0) and (i != (len(s)-1))):
            p += 1
            second_c = False

        if (c in dig) and (third_c) and ((i != 0) and (i != (len(s)-1))):
            p += 1
            third_c = False

        if (c in spec) and (fourth_c) and ((i != 0) and (i != (len(s)-1))):
            p += 1
            fourth_c = False

        if p == 5:
            break

    if p != 5:
        print("NO")
    else:
        print("YES")
