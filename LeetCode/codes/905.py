# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        r_even = []
        r_odd = []
        for i in A:
            if i%2:
                r_odd.append(i)
            else:
                r_even.append(i)
        return r_even + r_odd