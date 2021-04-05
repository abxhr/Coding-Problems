# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        max = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max:
                prev = max
                max = arr[i]
                arr[i] = prev
            else:
                arr[i] = max
        arr[-1] = -1
        return arr
