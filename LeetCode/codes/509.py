# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        f0 = 0
        f1 = 1
        n -= 1
        while(n):
            t = f1
            f1 = f1 + f0
            f0 = t
            n -= 1
        return f1
