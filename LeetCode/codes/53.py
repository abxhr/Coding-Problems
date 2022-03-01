# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_add = nums[0]
        for n in nums[1:]:
            curr_add = max(n, n+curr_add)
            max_sum = max(max_sum, curr_add)
        return max_sum