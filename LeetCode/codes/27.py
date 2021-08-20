# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while (i <= j):
            if nums[i] == val:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
            else:
                i += 1
        return i