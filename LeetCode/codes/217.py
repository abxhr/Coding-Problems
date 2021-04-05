# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
