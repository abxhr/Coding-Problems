# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                dup.append(n)
            nums[n - 1] = -1 * nums[n - 1]
        return dup 	