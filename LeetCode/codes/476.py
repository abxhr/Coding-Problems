# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num).split('b')[1]
        res = ""
        for n in num:
            if n == '1':
                res += "0"
            else:
                res += "1"
        return int(res, 2)