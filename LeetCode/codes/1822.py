# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                prod = prod * -1
        return prod