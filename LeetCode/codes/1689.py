# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def minPartitions(self, n: str) -> int:
        for i in "987654321":
            if i in n:
                return i
