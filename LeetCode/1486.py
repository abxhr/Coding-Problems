# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start+2*i)
        val = 0
        for i in nums:
            val = val ^ i
        return val
