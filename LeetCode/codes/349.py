# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))