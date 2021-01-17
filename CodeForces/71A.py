# Author: Abshar Mohammed Aslam, github.com/abxhr

n = int(input())
for i in range(n):
    w = input()
    if(len(w)>10):
    	wn = w[0] + str(len(w)-2) + w[-1]
    	print(wn)
    else:
    	print(w)