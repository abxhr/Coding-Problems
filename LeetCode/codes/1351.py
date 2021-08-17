# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid:
            for col in row:
                if col < 0:
                    total += 1
        return total
