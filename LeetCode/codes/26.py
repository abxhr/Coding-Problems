# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        loc = 1
        for ind in range(1, len(nums)):
            if nums[ind] != nums[ind - 1]:
                nums[loc] = nums[ind]
                loc += 1
        return loc