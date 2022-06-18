# Author: Abshar Mohammed Aslam, github.com/abxhr

def yes_no():
    n_x = list(map(int, input().split()))
    x = n_x[1]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort(reverse=True)
    c = True
    for i in range(len(b)):
        if not(a[i] + b[i] <= x):
            c = False
            break
    if c:
        print("Yes")
    else:
        print("No")


t = int(input())
for i in range(t-1):
    yes_no()
    ignore = input()
yes_no()
