# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            sq = 0
            while n > 0:
                digit = n % 10
                sq += digit ** 2
                n = n//10
            return sq
        used = [n]
        val = n
        while val != 1:
            val = square(val)
            if val in used:
                return False
            used.append(val)
        return True
