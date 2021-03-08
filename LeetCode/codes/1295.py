# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            s = str(i)
            l = 0
            for j in s:
                l += 1
            if (l%2==0):
                count += 1
        return count