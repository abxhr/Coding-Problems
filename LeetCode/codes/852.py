# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev = arr[0]
        for i in range(len(arr)):
            if arr[i] < prev:
                return i-1
            else:
                prev = arr[i]