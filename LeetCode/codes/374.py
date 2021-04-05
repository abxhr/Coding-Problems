# Author: Abshar Mohammed Aslam, github.com/abxhr

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while (l <= h):
            m = (l+h)//2
            g = guess(m)
            if g == -1:
                h = m - 1
            elif g == 1:
                l = m + 1
            else:
                return m
