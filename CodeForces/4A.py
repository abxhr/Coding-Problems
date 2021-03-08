# Author: Abshar Mohammed Aslam, github.com/abxhr

w=int(input())
y=0
f=0
m=int(w/2)
for i in range(m+1):
    y = w-i
    if(y==0 or i==0):
    	continue
    if (i%2 == 0):
    	if(y%2 == 0):
    		f=1
    		print("Yes")
    		break
if(f==0):
    print("NO")