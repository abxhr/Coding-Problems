# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        smax = 0
        for i in nums:
            if i >= max:
                smax = max
                max = i
            elif i >= smax:
                smax = i
        return ((max-1) * (smax-1))
