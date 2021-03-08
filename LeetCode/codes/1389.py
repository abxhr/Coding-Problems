# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst = lst[:index[i]] + [nums[i]] + lst[index[i]:]
        return(lst)
