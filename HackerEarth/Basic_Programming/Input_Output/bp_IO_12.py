# Author: Abshar Mohammed Aslam, github.com/abxhr

t = int(input())
while(t):
    n = int(input())
    s = input()
    vowels = list("aeiou")
    count = 0
    for i in range(n-1):
        if s[i] not in vowels:
            if s[i+1] in vowels:
                count += 1
    print(count)
    t -= 1
