x = int(input())
shoesizes = list(map(int, input().split()))
n = int(input())
money = 0
for i in range(n):
    ss_x = list(map(int, input().split()))
    if ss_x[0] in shoesizes:
        money += ss_x[1]
        shoesizes.remove(ss_x[0])
print(money)
