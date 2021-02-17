# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_sum = len(nums)
        lst_sum = 0
        for i in range(len(nums)):
            full_sum += i
            lst_sum += nums[i]
        return full_sum - lst_sum