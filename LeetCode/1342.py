# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def numberOfSteps (self, num: int) -> int:
        c = 0
        while num!= 0:
            if num % 2 == 0:
                num /= 2
                c += 1
            else:
                num -= 1
                c += 1
        return(c)
