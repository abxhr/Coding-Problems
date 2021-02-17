# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(int(len(nums)/2)):
            freq = nums[2*i]
            val = nums[2*i+1]
            for i in range(freq):
                lst.append(val)
        return(lst)
