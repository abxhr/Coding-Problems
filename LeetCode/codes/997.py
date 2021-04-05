# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        counts = [0] * N
        for i, j in trust:
            counts[i-1] -= 1
            counts[j-1] += 1
        for i, count in enumerate(counts):
            if count == N-1:
                return i+1
        return -1
