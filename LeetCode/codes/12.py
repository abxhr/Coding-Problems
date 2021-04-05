# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def intToRoman(self, num: int) -> str:
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC",
                 "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        for i in range(len(integer)):
            num, remainder = divmod(num, integer[i])
            res += num * roman[i]
            num = remainder
        return res
