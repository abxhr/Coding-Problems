# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        lsta = list(A[0])
        lstb = list(A[0])
        for i in range(1, len(A)):
            lsta = lstb
            lstb = []
            for j in A[i]:
                if j in lsta:
                    lstb.append(j)
                    lsta.remove(j)
        return lstb
