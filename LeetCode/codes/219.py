# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check={}
        for i in range(len(nums)):
            if nums[i] in check and abs(i-check[nums[i]])<=k:
                return True
            check[nums[i]]=i
        return False
