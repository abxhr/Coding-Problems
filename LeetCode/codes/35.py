# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start