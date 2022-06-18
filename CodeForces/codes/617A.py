# Author: Abshar Mohammed Aslam, github.com/abxhr

x = int(input())
steps = 0
while x > 0:
    for i in [5, 4, 3, 2, 1]:
        if x >= i:
            x -= i
            break
    steps += 1
print(steps)
