# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [i*i for i in nums]
        nums.sort()
        return nums