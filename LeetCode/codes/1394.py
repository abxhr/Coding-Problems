# Author: Abshar Mohammed Aslam

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max = -1
        counts = Counter(arr)
        for i,j in counts.items():
            if (i==j) and (i>max):
                max = i
        return max