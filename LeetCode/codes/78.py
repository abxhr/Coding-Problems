# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for n in nums:
            subs += [[n] + i for i in subs]
        return subs