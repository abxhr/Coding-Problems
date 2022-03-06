# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        
        i = 0
        j = 0
        k = 0
        if m == 0:
            while(j<n):
                nums1[k] = nums2[j]
                k += 1
                j += 1
            return
        
        nums = []
        for i in nums1:
            nums.append(i)
        while((i<m) and (j<n)):
            if (nums[i] <= nums2[j]):
                nums1[k] = nums[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        while(i<m):
            nums1[k] = nums[i]
            k += 1
            i += 1
        while(j<n):
            nums1[k] = nums2[j]
            k += 1
            j += 1
            