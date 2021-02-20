# Author: Abshar Mohammed Aslam, github.com/abxhr

import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for i in c.items():
            if i[1] != 2:
                return i[0]