# Author: Abshar Mohammed Aslam, github: @abxhr

steps = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2:
            return 2
        if n not in steps:
            steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return steps[n]