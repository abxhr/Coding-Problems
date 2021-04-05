# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dist = 0
        for i in range(len(arr1)):
            f = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    f = False
                    break
            if f:
                dist += 1
        return dist
