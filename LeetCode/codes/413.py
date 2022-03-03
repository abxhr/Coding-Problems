# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:          
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subarrays = 0
        curr = 1
        for ind in range(2, len(nums)):
            if (nums[ind] - nums[ind-1]) == (nums[ind-1] - nums[ind-2]):
                subarrays += curr
                curr += 1
            else:
                curr = 1
        return subarrays