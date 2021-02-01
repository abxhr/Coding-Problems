# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        a = s[:int(len(s)/2)]
        b = s[int(len(s)/2):]
        a_c = 0
        b_c = 0
        for i in range(len(a)):
            if a[i] in v:
                a_c += 1
            if b[i] in v:
                b_c += 1
        if a_c == b_c:
            return True
        else:
            return False