# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_lst = {min(i) for i in matrix}
        max_lst = {max(i) for i in zip(*matrix)}
        return min_lst & max_lst