# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            for j in range(len(i)):
                if j+1 <= (len(i)/2):
                    t = i[j]
                    i[j] = i[len(i)-1-j]
                    i[len(i)-1-j] = t
            
        for i in A:
            for j in range(len(i)):
                if i[j]:
                    i[j] = 0
                else:
                    i[j] = 1
        return A