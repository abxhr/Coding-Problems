# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        for i in range(len(nums1)):
            f = False
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j] > nums1[i]:
                    nums3.append(nums2[j])
                    f = True
                    break
            if not(f):
                nums3.append(-1)
        return nums3            