# Author: Abshar Mohammed Aslam, github.com/abxhr

a, b = map(int, input().split())
years = 0
while not(a > b):
    a *= 3
    b *= 2
    years += 1
print(years)