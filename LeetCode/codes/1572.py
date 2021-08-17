# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        v = int(len(mat))-1
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j:
                    sum += mat[i][j]
                elif i+j == v:
                    sum += mat[i][j]
        return sum
