# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        if '6' not in num:
            return int(num)
        num = list(num)
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        return int(''.join(num))
