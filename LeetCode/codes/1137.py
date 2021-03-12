# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        last = 0
        for i in range(n+1):
            last = t0
            new = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = new
        return last