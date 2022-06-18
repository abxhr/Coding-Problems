t = int(input())
for _ in range(t):
    k = 0
    a,b,c,d = list(map(int,input().split()))
    for i in [b,c,d]:
        if i > a:
            k += 1
    print(k)