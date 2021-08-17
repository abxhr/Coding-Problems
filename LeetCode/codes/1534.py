# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = 0
        for i in range(0, len(arr)-2):
            for j in range(1, len(arr)-1):
                for k in range(2, len(arr)):
                    if i < j < k:
                        if (abs(arr[i]-arr[j]) <= a) and (abs(arr[j]-arr[k]) <= b) and (abs(arr[i]-arr[k]) <= c):
                            n += 1
        return n
