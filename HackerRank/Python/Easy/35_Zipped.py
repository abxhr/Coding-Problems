# Author: Abshar Mohammed Aslam, github.com/abxhr

n, x = map(int, input().split())
marks = []
for _ in range(x):
    marks.append(list(map(float, input().split())))
for i in zip(*marks):
    print(sum(i)/len(i))
