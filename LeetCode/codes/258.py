# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def addDigits(self, num: int) -> int:
        digits = str(num)
        while len(digits) != 1:
            num = sum([int(i) for i in digits])
            digits = str(num)
        return int(num)
