# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])