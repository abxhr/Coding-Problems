# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]
