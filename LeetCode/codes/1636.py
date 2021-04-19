# Author: Absahr Mohammed Aslam, github.com/abxhr

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        return sorted(nums, key = nums.count)