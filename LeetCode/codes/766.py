# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = 0
        while i < len(matrix)-1:
            if matrix[i+1][1:] != matrix[i][:-1]:
                return False
            i += 1
        return True