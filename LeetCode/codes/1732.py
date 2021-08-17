# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        val = 0
        for i in gain:
            val += i
            if val > max:
                max = val
        return max
